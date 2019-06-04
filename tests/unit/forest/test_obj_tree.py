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

            # Compare children node -> self (recursive __ne__)
            for i in range(0, len(node.children)):
                if node.children[i] != self.children[i]:
                    return True

            # Compare children self -> node (recursive __ne__)
            for i in range(0, len(expected.children)):
                if expected.children[i] != actual.children[i]:
                    return True

            # Compare object values node -> self
            for k in node.val_dict.keys():
                if node.val_dict[k] !=  self.val_dict.get(k):
                    return True

            # Compare object values self -> node
            for k in self.val_dict.keys():
                if self.val_dict[k] != node.val_dict.get(k):
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
    # Can't be sure that this works and only one element
    # in the list is returned. Best to patch everything,
    # and let the assertion sort it out
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
        pass

    def test_inter_multi_obj(self):
        pass

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

        import pdb; pdb.set_trace()
        cut_tree = obj_tree._dfs_cut(test_dict, InterNode('fake_ref_0'))
        _init_patch(cut_tree)

        self.assertObjEquals([test_obj], cut_tree)

    def test_multi_obj_inter(self):
        pass

    def test_multi_inter_obj(self):
        pass

    def test_multi_mix_multi_mix(self):
        pass

class TestTransformTree(unittest.TestCase):
    pass


class TestParseTree(unittest.TestCase):
    pass
