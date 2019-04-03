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


class ForestGen(object):

    def __init__(self):
        self.obj_list = []

    def parse_tree(self, tree_obj):
        self.dfs_search(dfs_transform(tree_obj))
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

    def dfs_cut(self, obj):
        '''
        This iterates over the tree and extracts
        refrence objects out of it
        '''
        del_list = []
        vals = list(obj.values())
    
        if len(vals) == 1 and type(vals[0]) != dict:
            return
    
        self.obj_list.append(obj)
        inx = len(self.obj_list)-1
        for k,v in obj.items():
            if str(k)[-5:] == '-list':
                del_list.append(k)
                v.update({'refrence-object': k})
                dfs_search(v)
            elif type(v) == dict:
                dfs_cut(v)
    
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
