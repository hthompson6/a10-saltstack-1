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

    class Patcher(type(instance)):

        def __ne__(self, node):

            # Compare id's
            if self.id != node.id:
                return True

            # Compare parents (recursive __ne__)
            if self.parent != node.parent:
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

            return False

    instance.__class__ = Patcher


class TestCutTree(unittest.TestCase, CustomAssertions):
    '''
    In order to properly test how these nodes are built,
    these test cases must take the form of intergration tests as
    the dependency on the node module is not mocked.
    '''

    def test_l0(self):
        test_obj = {}
        cut_tree = obj_tree._dfs_cut(test_obj)
        self.assertEqual(None, cut_tree)

    def test_l1(self):
        test_obj = {'fake_key': 'fake_val'}
        cut_tree = obj_tree._dfs_cut(test_obj)
        self.assertEquals(None, cut_tree)

    def test_l2(self):
        key_vals = {'fake_ref': {'fake_key': 'fake_val'}}
        test_dict = {'obj_id': key_vals} 
        test_obj = ObjNode('obj_id', **key_vals)
        _patch_ne(test_obj)

        helper.get_ref_props = Mock(return_value={})
        obj_tree._extract_modname = Mock(return_value='fake_ref')

        cut_tree = obj_tree._dfs_cut(test_dict)

        # Can't be sure that this works and only one element
        # in the list is returned. Best to patch everything,
        # and let the assertion sort it out.
        for node_obj in cut_tree:
            _patch_ne(node_obj)

        self.assertObjEquals([test_obj], cut_tree)


class TestTransformTree(unittest.TestCase):
    pass


class TestParseTree(unittest.TestCase):
    pass
