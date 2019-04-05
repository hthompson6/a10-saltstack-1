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


class ForestGen(object):

    def _extract_modname(self, url):
        url = url.replace('/axapi/v3/', '').replace('/',
            '_').replace('-', '_').replace('+', '')
        url = re.sub(r'_{[a-zA-Z_]+}|{[a-zA-Z_]+}', '', url) 
        return "a10_{url}".format(url=url)

    def __init__(self):
        self.obj_list = []

    def parse_tree(self, tree_obj):
        self.dfs_cut(self.dfs_transform(tree_obj), 0)
        self.trim_excess()
        return self.obj_list

    def trim_excess(self):
        '''
        Hacky solution to remove excess dictionaries
        that don't have parent objects
        '''
        for x in range(1, len(self.obj_list)-1):
            vals = list(self.obj_list[x].values())
            if len(vals) == 1 and type(vals[0]) != dict:
                del self.obj_list[x]

    def dfs_cut(self, obj, parent_index, fdqn=nul):
        '''
        This iterates over the tree and extracts
        refrence objects out of it
        '''
        del_list = []
        vals = list(obj.values())

        if len(vals) == 1 and type(vals[0]) != dict:
            return

        obj.update({'parent-index': parent_index})
        self.obj_list.append(obj)
        inx = len(self.obj_list)-1

        if fdqn:
            ref_props = a10_helper.get_ref_props(fdqn)
        else:
            ref_props = {}

        for k,v in obj.items():
            if k in ref_props:
                del_list.append(k)
                mod_fdqn = _extract_modname(ref_props[k])
                v.update({'$ref': mod_fdqn})
                self.dfs_cut(v, inx, mod_fdqn)
            elif type(v) == dict:
                self.dfs_cut(v, inx)

        for i in del_list:
            del self.obj_list[inx][i]
 
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
