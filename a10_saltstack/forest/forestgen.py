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
import importlib
import re

from a10_saltstack.helpers import helper as a10_helper
from a10_saltstack.forest.nodes import InterNode, ObjNode, RootNode

class ForestGen(object):

    def _extract_modname(self, url):
        url = url.replace('/axapi/v3/', '').replace('/',
            '_').replace('-', '_').replace('+', '')
        url = re.sub(r'_{[a-zA-Z_]+}|{[a-zA-Z_]+}', '', url) 
        return "a10_{url}".format(url=url)

    def __init__(self):
        self.obj_list = []

    def parse_tree(self, a10_obj, tree_obj):
        a10_obj = 'a10_{}'.format(a10_obj)

        root = RootNode(tree_obj['a10_name'], a10_obj)

        self.dfs_cut(self.dfs_transform(tree_obj), root)
        self.trim_excess()
        root.addValDict(**self.obj_list[0])

        return root 

    def trim_excess(self):
        '''
        Hacky solution to remove excess dictionaries
        that don't have parent objects
        '''
        cnt = 0
        while cnt < len(self.obj_list):
            vals = list(self.obj_list[cnt].keys())
            if len(vals) == 1 and type(vals[0]) != dict:
                del self.obj_list[cnt]
                cnt -= 1
            cnt += 1

    def dfs_cut(self, obj, refNode=None):
        '''
        This iterates over the tree and extracts
        refrence objects out of it
        '''
        vals = list(obj.values())

        if len(vals) == 1 and type(vals[0]) != dict:
            return

        if refNode:
            ref_props = a10_helper.get_ref_props(refNode.ref)
        else:
            ref_props = {}

        node_list = []
        for k,v in obj.items():
            if k in ref_props:
                mod_fqdn = self._extract_modname(ref_props[k])
                inNode = InterNode(k, mod_fqdn)
                child_obj_list = self.dfs_cut(v, inNode)
                if child_obj_list:
                    for child in child_obj_list:
                        inNode.addChild(child)
                node_list.append(inNode)

            elif type(v) == dict:
                tempNode = ObjNode(k, **v)
                child_obj_list = self.dfs_cut(v, refNode)
                if child_obj_list:
                    for child in child_obj_list:
                        tempNode.addChild(child)
                node_list.append(tempNode)

        return node_list

    def dfs_transform(self, obj):
        '''
        This is used to turn the OrderedDicts
        into normal dicts, and extract lists
        into dicts
        '''
        obj = dict(obj)
        for k,v in obj.items():
            new_dict = {}
            if type(v) == list:
               for i in v:
                   new_dict.update(self.dfs_transform(i))
               obj[k] = new_dict
            if type(v) == OrderedDict:
               new_dict.update(self.dfs_transform(v)) 
               obj[k] = new_dict
        return obj

tree_obj = {'netmask': '255.255.255.0', 'port_list': [OrderedDict([(22, [OrderedDict([('protocol', 'tcp')])])]), OrderedDict([(80, [OrderedDict([('protocol', 'tcp')])])]), OrderedDict([('service_group', [OrderedDict([('sg1', [OrderedDict([('member_list', [OrderedDict([('mem1', [OrderedDict([('host', '10.7.11.1')])])]), OrderedDict([('mem2', [OrderedDict([('host', '10.7.11.2')])])])])]), OrderedDict([('lb_type', 'round_robin')])])])])])], 'a10_name': 'vs2', 'ip_address': '192.168.43.6', 'a10_obj': 'slb_virtual_server', 'name': 'VS2'}

frst = ForestGen()
frst.parse_tree('slb_virtual_server', tree_obj)
