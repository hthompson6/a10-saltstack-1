# Copyright 2019 A10 Networks
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from collections import OrderedDict
from mock import Mock
import unittest

import a10_saltstack.forest.nodes
from a10_saltstack.forest import obj_tree
from a10_saltstack.helpers import helper

from a10_saltstack.forest.nodes import ObjNode, InterNode
from tests.unit.forest.custom_assertions import CustomAssertions
from tests.unit.forest import fake_obj_dict as fobj


def _patch_ne(instance):

    class BasePatcher(type(instance)):

        def _safe_ne_comp(self, node):
            '''
            Meant to only be used when comparing two parent nodes.
            Does not include a comparison of children as this
            leads to an infinite recursive loop.
            '''
            if type(self) != type(node):
                return True

            if isinstance(instance, InterNode):
                if self.ref != node.ref:
                    return True                
            elif isinstance(instance, ObjNode):
                if self.id != node.id:
                    return True

            if self.parent._safe_ne_comp(node.parent):
                return True

            if len(self.children) != len(node.children):
                return True

            # Compare object values node -> self
            for k in node.val_dict.keys():
                if node.val_dict[k] != self.val_dict.get(k):
                    return True

            # Compare object values self -> node
            for k in self.val_dict.keys():
                if self.val_dict[k] != node.val_dict.get(k):
                    return True

            return False

        def __ne__(self, node):
            if type(self) != type(node):
                return True

            if self.parent._safe_ne_comp(node.parent):
                return True

            # Compare length of child lists
            if len(self.children) != len(node.children):
                return True

            # Need to compare lists which are spawned off dictionary.
            # So convert them back to dictionary.
            child_dict = {}
            node_child_dict = {}

            for child in node.children:
                if hasattr(child, 'id'):
                    node_child_dict[child.id] = child
                elif hasattr(child, 'ref'):
                    node_child_dict[child.ref] = child

            for child in self.children:
                if hasattr(child, 'id'):
                    child_dict[child.id] = child
                elif hasattr(child, 'ref'):
                    child_dict[child.ref] = child

            for k in expected_dict.keys():
                if expected_dict[k] !=  actual_dict.get(k):
                    return True

            # Compare length of val_dicts
            if len(self.val_dict) != len(node.val_dict):
                return True

            # Compare val_dicts
            for k in self.val_dict.keys():
                if self.val_dict[k] !=  node.val_dict.get(k):
                    return True

    class ObjPatcher(BasePatcher):

        def __ne__(self, node):
            super(ObjPatcher, self).__ne__(node)

            if self.id != node.id:
                return True

            return False

    class InterPatcher(BasePatcher):

        def __ne__(self, node):
            super(InterPatcher, self).__ne__(node)

            if self.ref != node.ref:
                return True

            return False

    if type(instance) == ObjNode:
        instance.__class__ = ObjPatcher

    if type(instance) == InterNode:
        instance.__class__ = InterPatcher


def _preform_patch(node):
    for child in node.children:
        _preform_patch(child)
    _patch_ne(node)


def _init_patch(tree):
    for node in tree:
        _preform_patch(node)


class TestCutTree(unittest.TestCase, CustomAssertions):
    '''
    In order to properly test how these nodes are built,
    these test cases must take the form of intergration tests as
    the dependency on the node module is not mocked.
    '''

    def setUp(self):
        obj_tree._extract_modname = lambda x: x

    def test_empty(self):
        test_obj = {}
        cut_tree = obj_tree._dfs_cut(test_obj)
        self.assertEqual(None, cut_tree)

    def test_kv(self):
        test_obj = {'fake_key': 'fake_val'}
        cut_tree = obj_tree._dfs_cut(test_obj)
        self.assertEquals(None, cut_tree)

    def test_inter(self):
        key_vals = {'fake_key': 'fake_val'}
        test_dict = {'fake_ref': key_vals}

        test_inter = InterNode('fake_path', **key_vals)
        _patch_ne(test_inter)

        helper.get_ref_props = Mock(return_value={'fake_ref': 'fake_path'})

        # test_inter is passed here to take the place of the root node
        cut_tree = obj_tree._dfs_cut(test_dict, test_inter)
        _init_patch(cut_tree)

        self.assertObjEquals([test_inter], cut_tree)

    def test_obj(self):
        key_vals = {'fake_key': 'fake_val'}
        test_dict = {'obj_id': key_vals}

        test_obj = ObjNode('obj_id', **key_vals)
        _patch_ne(test_obj)

        helper.get_ref_props = Mock(return_value={})

        cut_tree = obj_tree._dfs_cut(test_dict)
        _init_patch(cut_tree)

        self.assertObjEquals([test_obj], cut_tree)

    def test_obj_no_ref_call(self):
        key_vals = {'fake_key': 'fake_val'}
        test_dict = {'obj_id': key_vals}

        test_obj = ObjNode('obj_id', **key_vals)
        _patch_ne(test_obj)

        helper.get_ref_props = Mock(return_value={})
        cut_tree = obj_tree._dfs_cut(test_dict)

        helper.get_ref_props.assert_not_called()

    def test_inter_obj(self):
        key_vals = {'fake_key': 'fake_val'}
        test_dict = {'fake_ref': {'obj_id': key_vals}}

        test_obj = ObjNode('obj_id', **key_vals)
        test_inter = InterNode('fake_path')
        _patch_ne(test_obj)
        _patch_ne(test_inter)

        test_obj.addParent(test_inter)
        test_inter.addChild(test_obj)

        helper.get_ref_props = Mock(return_value={'fake_ref': 'fake_path'})

        # test_inter is passed here to take the place of the root node
        cut_tree = obj_tree._dfs_cut(test_dict, test_inter)
        _init_patch(cut_tree)

        self.assertObjEquals([test_inter], cut_tree)

    def test_obj_inter(self):
        key_vals = {'fake_key': 'fake_val'}
        test_dict = {'obj_id': {'fake_ref': key_vals}}

        test_obj = ObjNode('obj_id')
        test_inter = InterNode('fake_path', **key_vals)
        _patch_ne(test_obj)
        _patch_ne(test_inter)

        test_inter.addParent(test_obj)
        test_obj.addChild(test_inter)

        helper.get_ref_props = Mock(return_value={'fake_ref': 'fake_path'})

        # test_inter is passed here to take the place of the root node
        cut_tree = obj_tree._dfs_cut(test_dict, test_inter)
        _init_patch(cut_tree)

        self.assertObjEquals([test_obj], cut_tree)

    def test_obj_obj(self):
        key_vals = {'fake_key': 'fake_val'}
        test_dict = {'obj_id': {'obj_id_2': key_vals}}

        test_obj = ObjNode('obj_id')
        test_obj_2 = ObjNode('obj_id_2', **key_vals)
        _patch_ne(test_obj)
        _patch_ne(test_obj_2)

        test_obj_2.addParent(test_obj)
        test_obj.addChild(test_obj_2)

        cut_tree = obj_tree._dfs_cut(test_dict)
        _init_patch(cut_tree) 

        self.assertObjEquals([test_obj], cut_tree)

    def test_inter_inter(self):
        key_vals = {'fake_key': 'fake_val'}
        test_dict = {'fake_ref_0': {
            'fake_ref_1': key_vals}}

        test_inter = InterNode('fake_path_0')
        _patch_ne(test_inter)
 
        test_inter_2 = InterNode('fake_path_1', **key_vals)
        _patch_ne(test_inter_2)
        test_inter_2.addParent(test_inter)
        test_inter.addChild(test_inter_2)

        helper.get_ref_props = Mock(return_value={
            'fake_ref_0': 'fake_path_0',
            'fake_ref_1': 'fake_path_1'})

        cut_tree = obj_tree._dfs_cut(test_dict, InterNode('fake_ref_0'))
        _init_patch(cut_tree)

        self.assertObjEquals([test_inter], cut_tree)

    def test_inter_multi_obj(self):
        key_vals = {'fake_key': 'fake_val'}
        test_dict = {'fake_ref': {
            'obj_id_0': key_vals,
            'obj_id_1': key_vals,
            'obj_id_2': key_vals}}

        test_inter = InterNode('fake_path')
        _patch_ne(test_inter)
        for i in range(0, 3):
            temp_obj = ObjNode('obj_id_{}'.format(i), **key_vals)
            _patch_ne(temp_obj)
            temp_obj.addParent(test_inter)
            test_inter.addChild(temp_obj)

        helper.get_ref_props = Mock(return_value={
            'fake_ref': 'fake_path'})

        cut_tree = obj_tree._dfs_cut(test_dict, test_inter)
        _init_patch(cut_tree)

        self.assertObjEquals([test_inter], cut_tree)

    def test_obj_multi_inter(self):
        key_vals = {'fake_key': 'fake_val'}
        test_dict = {'obj_id': {
            'fake_ref_0': key_vals,
            'fake_ref_1': key_vals,
            'fake_ref_2': key_vals}}

        test_obj = ObjNode('obj_id')
        _patch_ne(test_obj)
        for i in range(0, 3):
            temp_inter = InterNode('fake_path_{}'.format(i), **key_vals)
            _patch_ne(temp_inter)
            temp_inter.addParent(test_obj)
            test_obj.addChild(temp_inter)

        helper.get_ref_props = Mock(return_value={
            'fake_ref_0': 'fake_path_0',
            'fake_ref_1': 'fake_path_1',
            'fake_ref_2': 'fake_path_2'})

        cut_tree = obj_tree._dfs_cut(test_dict, InterNode('fake_ref_0'))
        _init_patch(cut_tree)

        self.assertObjEquals([test_obj], cut_tree)

    def test_multi_obj_inter(self):
        key_vals = {'fake_key': 'fake_val'}
        inter_dict = {'fake_ref': key_vals}
        test_dict = {'obj_id_0': inter_dict,
                     'obj_id_1': inter_dict,
                     'obj_id_2': inter_dict}

        node_list = []
        for i in range(0, 3):
            temp_obj = ObjNode('obj_id_{}'.format(i))
            temp_inter = InterNode('fake_path', **key_vals)

            _patch_ne(temp_obj)
            _patch_ne(temp_inter)

            temp_inter.addParent(temp_obj)
            temp_obj.addChild(temp_inter)
            node_list.append(temp_obj)

        helper.get_ref_props = Mock(return_value={
            'fake_ref': 'fake_path'})

        cut_tree = obj_tree._dfs_cut(test_dict, InterNode('fake_ref'))
        _init_patch(cut_tree)

        self.assertObjEquals(node_list, cut_tree)

    def test_multi_inter_obj(self):
        key_vals = {'fake_key': 'fake_val'}
        obj_dict = {'obj_id': key_vals}
        test_dict = {'fake_ref_0': obj_dict,
                     'fake_ref_1': obj_dict,
                     'fake_ref_2': obj_dict}

        node_list = []
        for i in range(0, 3):
            temp_inter = InterNode('fake_path_{}'.format(i))
            temp_obj = ObjNode('obj_id', **key_vals)

            _patch_ne(temp_obj)
            _patch_ne(temp_inter)

            temp_obj.addParent(temp_inter)
            temp_inter.addChild(temp_obj)
            node_list.append(temp_inter)

        helper.get_ref_props = Mock(return_value={
            'fake_ref_0': 'fake_path_0',
            'fake_ref_1': 'fake_path_1',
            'fake_ref_2': 'fake_path_2'})

        cut_tree = obj_tree._dfs_cut(test_dict, InterNode('fake_ref_0'))
        _init_patch(cut_tree)

        self.assertObjEquals(node_list, cut_tree)

    def test_multi_mix_multi_mix(self):
        key_vals = {'fake_key': 'fake_val'}
        test_dict = {'fake_ref_0': {'obj_id_1': key_vals,
                                    'fake_ref_2': key_vals},
                     'obj_id_0': {'fake_ref_3': key_vals,
                                  'fake_ref_4': key_vals,
                                  'obj_id_2': key_vals},
                     'fake_ref_1': {'obj_id_3': key_vals}}

        inter_0 = InterNode('fake_path_0')
        inter_1 = InterNode('fake_path_1')
        inter_2 = InterNode('fake_path_2', **key_vals)
        inter_3 = InterNode('fake_path_3', **key_vals)
        inter_4 = InterNode('fake_path_4', **key_vals)

        obj_0 = ObjNode('obj_id_0')
        obj_1 = ObjNode('obj_id_1', **key_vals)
        obj_2 = ObjNode('obj_id_2', **key_vals)
        obj_3 = ObjNode('obj_id_3', **key_vals)

        inter_node_list = [inter_0, inter_1, inter_2, inter_3, inter_4]
        _init_patch(inter_node_list)

        obj_node_list = [obj_0, obj_1, obj_2, obj_3]
        _init_patch(obj_node_list)

        inter_0.addChild(obj_1)
        inter_0.addChild(inter_2)
        obj_0.addChild(inter_3)
        obj_0.addChild(inter_4)
        obj_0.addChild(obj_2)
        inter_1.addChild(obj_3)

        node_list = [inter_0, obj_0, inter_1]

        helper.get_ref_props = Mock(return_value={
            'fake_ref_0': 'fake_path_0',
            'fake_ref_1': 'fake_path_1',
            'fake_ref_2': 'fake_path_2',
            'fake_ref_3': 'fake_path_3',
            'fake_ref_4': 'fake_path_4'})

        cut_tree = obj_tree._dfs_cut(test_dict, InterNode('fake_ref_0'))
        _init_patch(cut_tree)

        self.assertObjEquals(node_list, cut_tree)


class TestTransformTree(unittest.TestCase):

    def _odict(self, *args):
        '''
        Writing out OrderedDict makes the code look messy.
        This function has been added to address that.

        Args:
            args: vals added to the OrderedDict as kv pairs
        Returns (OrderedDict):
        '''
        if type(args) == tuple:
            return OrderedDict([args])
        if type(args) == list:
            return OrderedDict(args)
        elif len(args) == 2:
            return OrderedDict([(*args)])
        else:
            raise Exception

    def test_l0_odict_to_dict(self):
        test_arg = self._odict('fake_key', 'fake_val')
        expected = {'fake_key': 'fake_val'}
        actual = obj_tree._dfs_transform(test_arg)

        self.assertEquals(expected, actual) 

    def test_l1_list_nochange(self):
        test_arg = self._odict('fake_key', [1, 2, 3])
        expected = {'fake_key': [1, 2, 3]}
        actual = obj_tree._dfs_transform(test_arg)

        self.assertEquals(expected, actual)

    def test_l1_dict_nochange(self):
        test_arg = self._odict('fake_key', {'fake_key': 'fake_val'})
        expected = {'fake_key': {'fake_key': 'fake_val'}}
        actual = obj_tree._dfs_transform(test_arg)

        self.assertEquals(expected, actual)

    def test_l1_l0_odict_to_dict(self):
        test_val = self._odict('fake_key', 'fake_val')
        test_arg = self._odict('fake_key', test_val)
        expected = {'fake_key': {'fake_key': 'fake_val'}}
        actual = obj_tree._dfs_transform(test_arg)

        self.assertEquals(expected, actual)

    def test_l1_dict_list_nochange(self):
        test_kv = {'fake_key': 'fake_val'}
        test_arg = self._odict('fake_ref', [test_kv])
        expected = {'fake_ref': [{'fake_key': 'fake_val'}]}
        actual = obj_tree._dfs_transform(test_arg)

        self.assertEquals(expected, actual)

    def test_l1_odict_list_to_dict(self):
        test_val = self._odict('fake_key', 'fake_val')
        test_arg = self._odict('fake_ref', [test_val])
        expected = {'fake_ref': {'fake_key': 'fake_val'}}
        actual = obj_tree._dfs_transform(test_arg)

        self.assertEquals(expected, actual)

    def test_l1(self):
        test_val_0 = self._odict('fake_key', 'fake_val')
        test_val_1 = self._odict('fake_key_0', 'fake_val')
        test_val_2 = self._odict('fake_key_1', 'fake_val')
        test_arg = self._odict('fake_ref', [test_val_0, [test_val_1, test_val_2]])
        expected = {'fake_ref': [{'fake_key', 'fake_val'},
            {'fake_key_0': 'fake_val', 'fake_key_1': 'fake_val'}]}
        actual = obj_tree._dfs_transform(test_arg)

class TestParseTree(unittest.TestCase):
    pass
