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

from a10_saltstack.client.kwbl import KW_OUT, translate_blacklist as translateBlacklist
from a10_saltstack.client import errors as a10_ex
from a10_saltstack.forest.forest_gen import ForestGen
from a10_saltstack.forest.nodes import InterNode
from a10_saltstack.forest import obj_tree
from a10_saltstack.helpers import helper as a10_helper


def _build_envelope(title, data):
    return {
        title: data
    }


def _to_axapi(key):
    return translateBlacklist(str(key), KW_OUT).replace("_", "-")


def _build_dict_from_param(param):
    '''
    Converts the underscores of each dictionary key to dashes
    using the _to_axapi helper function.

    Args:
        param (dict): dictionary to be sanitized 

    Returns (dict):
        Sanitized dictionary
    '''
    rv = {}

    for k, v in param.items():
        hk = _to_axapi(k)
        if isinstance(v, dict):
            v_dict = _build_dict_from_param(v)
            rv[hk] = v_dict
        if isinstance(v, list):
            nv = [_build_dict_from_param(x) for x in v]
            rv[hk] = nv
        else:
            rv[hk] = v

    return rv


def _build_json(title, avail_props, **kwargs):
    '''
    Builds a json object from the provided kwargs using
    the provided property list.

    Args:
        title (string): generic name of the ACOS object
        avail_props (list): propeties of the ACOS object
        **kwargs: arbitrary values that make up the given ACOS object

    Returns (dict):
        JSON parsable dict that matches the format of the
        expected payload for the given ACOS object.
    '''
    rv = {}

    for x in avail_props:
        v = kwargs.get(x)
        if v:
            rx = _to_axapi(x)

            if isinstance(v, dict):
                nv = _build_dict_from_param(v)
                rv[rx] = nv
            if isinstance(v, list):
                nv = [_build_dict_from_param(x) for x in v]
                rv[rx] = nv
            else:
                rv[rx] = kwargs[x]

    return _build_envelope(title, rv)


def _build_obj_dict(tree_node, ref):
    '''
    Resolves url parameters using id of the current node
    and its parents.

    /url/entry/{parent1_name}/more/{parent2_name}/path/{child_name}+{child_val}

    As parent 1 is higher on the tree than parent 2, iteration needs to start from the
    tail end of the url and up towards the beginning. However, the keys have been stored
    from lowest to highest in the tree. So, iteration occurs from left to right over the array.

    Args:
        tree_node (object): an arbitrary node of the tree 
        ref (string): refrence module

    Returns (dict):
        Configuration values of a given ACOS object 
    '''
    child_keys = a10_helper.get_child_keys(ref)
    parent_keys = a10_helper.get_parent_keys(ref)

    for ck in child_keys:
        if ck not in tree_node.val_dict:
            tree_node.val_dict[ck] = tree_node.id

    pk = 0
    tempNode = tree_node.parent
    while pk < len(parent_keys) and tempNode != None:
        if not isinstance(tempNode, InterNode):
            tree_node.val_dict[parent_keys[pk]] = tempNode.id
            pk += 1
        tempNode = tempNode.parent

    tree_node.val_dict['ref'] = ref 
    return tree_node.val_dict


def parse_config(a10_obj_type, api, client, *args):
    '''
    Passes configuration onto processing functions. Preforms
    CRUD calls per object.

    Args:
        a10_obj_type (string): root ACOS object being operated on
        api (string): config api to access
        client (object): AXAPI REST client 
        *args: list of values and child objects of root object 

    Returns (dict):
        post/delete results 
    '''
    a10_obj = '{}_{}'.format(api, a10_obj_type)

    config = {}
    for k in args:
        config.update(k)

    root = obj_tree.parse_tree(a10_obj, config)
    forest_list = [root]

    forest = ForestGen()
    forest.dfs_cut(root)
    if forest.node_list:
        forest_list.extend(forest.node_list)

    obj_dict_list = []
    for tree in forest_list:
        if isinstance(tree, InterNode):
            for child in tree.children:
                if not isinstance(child, InterNode):
                    obj_dict_list.append(_build_obj_dict(child, tree.ref))
        else:
            obj_dict_list.append(_build_obj_dict(tree, tree.ref))


    post_result = {}
    cnt = 0

    # As objects with the most dependencies are at the top,
    # we will need to delete the objects starting at the bottom
    # of the object tree. 
    for i in range(len(obj_dict_list)-1, 0, -1):
        if obj_dict_list[i].get('absent'):
            ref = obj_dict_list[i]['ref']
            del obj_dict_list[i]['ref']
            existing_url = a10_helper.existing_url(ref, **obj_dict_list[i])
  
            ref = '{}_{}'.format(ref, cnt)
            post_result[ref] = client.delete(existing_url)
            del obj_dict_list[i]
            cnt += 1

    for a10_obj_val in obj_dict_list:
        ref = a10_obj_val['ref']
        del a10_obj_val['ref']

        avail_props = a10_helper.get_props(ref)
        obj_type = a10_helper.get_obj_type(ref)

        existing_url = a10_helper.existing_url(ref, **a10_obj_val)
        new_url = a10_helper.new_url(ref, **a10_obj_val)

        parent_keys = a10_helper.get_parent_keys(ref)

        del_list = []
        a10_obj_fin = {}
        for k,v in a10_obj_val.items():
            if k not in parent_keys:
                a10_obj_fin[k.replace('-', '_')] = v

        payload = _build_json(obj_type, avail_props, **a10_obj_fin)

        create = False
        try:
            need_update = False
            resp = client.get(existing_url)
            for k,v in a10_obj_fin.items():
               if k.replace('_', '-') in resp[obj_type]:
                    if v != resp[obj_type][k.replace('_', '-')]:
                        need_update = True
                        break
            if need_update:
                ref = '{}_{}'.format(ref, cnt)
                post_result[ref] = client.post(existing_url, payload)
        except a10_ex.NotFound:
            create = True

        if create:
            ref = '{}_{}'.format(ref, cnt)
            post_result[ref] = client.post(new_url, payload)
        cnt += 1

    return post_result
