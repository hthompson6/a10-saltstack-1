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

from a10_saltstack.forest import obj_tree
from a10_saltstack.helpers import helper
import a10_saltstack.forest.nodes
from a10_saltstack.forest.nodes import ObjNode, InterNode
from tests.unit.forest import fake_obj_dict as fobj


class TestCutTree(unittest.TestCase):

    def setUp(self):
        obj_tree._extract_modname = Mock()

    def test_empty(self):
        test_obj = {}
        cut_tree = obj_tree._dfs_cut(test_obj)
        self.assertEqual(None, cut_tree)

    def test_param(self):
        test_obj = {'fake_key': 'fake_val'}
        cut_tree = obj_tree._dfs_cut(test_obj)
        self.assertEquals(None, cut_tree)

    def test_obj_node(self):
        # Build test objects
        key_vals = {'fake_key': 'fake_val',
                    'fake_key2': 'fake_val'}
        test_dict = {'obj_id': key_vals} 
        test_obj = ObjNode('obj_id', **key_vals)

        # Mock out dependencies
        helper.get_ref_props = Mock(return_value={})
        a10_saltstack.forest.nodes.ObjNode = Mock(return_value=[test_obj]) 

        # Compare
        import pdb; pdb.set_trace()
        cut_tree = obj_tree._dfs_cut(test_dict)
        self.assertEquals([test_obj], cut_tree)

    def test_inter_node(self):
        test_dict = {'ref_id': {'fake_key': 'fake_val'}}

    def test_inter_obj(self):
        pass


class TestTransformTree(unittest.TestCase):
    pass


class TestParseTree(unittest.TestCase):
    pass
