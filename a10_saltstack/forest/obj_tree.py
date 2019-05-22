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
import logging
import re

from a10_saltstack.helpers import helper as a10_helper
from a10_saltstack.forest.nodes import InterNode, ObjNode, RootNode

LOG = logging.getLogger(__file__)


def _extract_modname(url):
    '''
    Converts the given refrence object url into the name
    of the corresponding python module.

    Args:
        url (string): refrence object url

    Returns (string):
        Name of python module related to refrence object
    '''
    url = url.replace('/axapi/v3/', '').replace('/',
        '_').replace('-', '_').replace('+', '')
    module_name = re.sub(r'_{[a-zA-Z_]+}|{[a-zA-Z_]+}', '', url) 
    return "a10_{mod}".format(mod=module_name)


def _dfs_cut(config, refNode=None):
    '''
    This iterates over the config and converts the dictionaries
    into nodes of a tree.

    Args:
        config (dict): configuration data

    Returns (list):
        List comprised of each node in the tree. Left side has
        the highest nodes and right side has the lowest nodes.
    '''

    if not isinstance(config, dict):
        return

    vals = list(config.values())
    if not len(vals):
        return

    if len(vals) == 1 and not isinstance(vals[0], dict):
        return

    if refNode:
        ref_props = a10_helper.get_ref_props(refNode.ref)
    else:
        ref_props = {}

    node_list = []
    for k,v in config.items():
        if k in ref_props:
            mod_fqdn = _extract_modname(ref_props[k])

            # Only case in which the keyword is not a string
            # is when the keyword is being used as an identifier.
            # These id's do not need to be store within the InterNode
            # at this point. 
            inter_val_dict = {}
            if isinstance(v, dict):
                for kw, vl in v.items():
                    if isinstance(kw, str):
                        inter_val_dict[kw] = vl
            inNode = InterNode(mod_fqdn, **inter_val_dict)

            child_obj_list = _dfs_cut(v, inNode)
            if child_obj_list:
                for child in child_obj_list:
                    inNode.addChild(child)
            node_list.append(inNode)

        elif isinstance(v, dict):
            tempNode = ObjNode(k, **v)
            child_obj_list = _dfs_cut(v, refNode)
            if child_obj_list:
                for child in child_obj_list:
                    tempNode.addChild(child)
            node_list.append(tempNode)

    return node_list


def _dfs_transform(config):
    '''
    This is used to turn the OrderedDicts into normal dicts, and extract lists
    into dicts.

    Args:
        config (OrderedDict): configuration data

    Returns (dict):
        Configuration data
    '''
    config = dict(config)
    for k,v in config.items():
        new_dict = {}
        if isinstance(v, list):
           for i in v:
               if isinstance(i, OrderedDict):
                   new_dict.update(_dfs_transform(i))
           if new_dict:
               config[k] = new_dict
           else:
               config[k] = v
        elif isinstance(v, OrderedDict):
           new_dict.update(_dfs_transform(v)) 
           config[k] = new_dict

    return config


def parse_tree(a10_obj, config):
    '''
    Converts the given configuration into a tree using
    the dfs_cut and dfs_transform helper functions. Creates a
    root node to which the rest of the configuration tree is attached.

    Args:
        a10_obj (string):
        config (OrderedDict): 

    Returns (object):
        Root node of the tree 
    '''
    a10_obj = 'a10_{}'.format(a10_obj)


    root = RootNode(None, a10_obj)
    altered_config = _dfs_transform(config)

    root_vals = {}
    for k,v in altered_config.items():
        if k == "a10_name":
            root.id = v
        elif k == "a10_obj":
            root.ref = a10_obj
        elif not isinstance(v, dict) and k != "name":
            root_vals[k] = v

    root.addValDict(**root_vals)

    if len(alterted_config) < 2:
        root_children = []
    else:
        root_children = _dfs_cut(altered_config, root)

    if root_children:
        for child in root_children:
            root.addChild(child)

    return root
