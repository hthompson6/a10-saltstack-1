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
    return translateBlacklist(key, KW_OUT).replace("_", "-")


def _build_dict_from_param(param):
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


def _build_obj_dict(forest_node, ref):
    child_keys = a10_helper.get_child_keys(ref)
    parent_keys = a10_helper.get_parent_keys(ref)

    for ck in child_keys:
        if ck not in forest_node.val_dict:
            forest_node.val_dict[ck] = forest_node.id

    pk = 0
    tempNode = forest_node.parent
    while pk < len(parent_keys) - 1:
        if type(tempNode) != InterNode:
            forest_node.val_dict[parent_keys[pk]] = tempNode.id
            pk -= 1
        tempNode = tempNode.parent

    return forest_node.val_dict

def parse_obj(a10_obj_type, op_type, client, **kwargs):
    root = obj_tree.parse_tree('{}_{}'.format(op_type, a10_obj_type), kwargs)
    forest_list = [root]

    forest = ForestGen()
    forest.dfs_cut(root)
    if forest.node_list:
        forest_list.extend(forest.node_list)


    #import pdb; pdb.set_trace()

    obj_dict_list = []
    for tree in forest_list:
        if type(tree) == InterNode:
            for child in tree.children:
                if type(child) != InterNode:
                    obj_dict_list.append(_build_obj_dict(child, tree.ref))
        else:
            obj_dict_list.append(_build_obj_dict(tree, tree.ref))

    for tree in forest_list: 
        url = a10_helper.get_url(tree['a10_obj'], op_type, **kwargs)
        avail_props = a10_helper.get_props(tree['a10_obj'], **kwargs)
        obj_type = a10_helper.get_obj_type(tree['a10_obj'])

        post_result = {}
        payload = _build_json(obj_type, avail_props, **kwargs)
        if payload[obj_type].get('a10-name'):
            payload[obj_type]["name"] = payload[obj_type]["a10-name"]
            del payload[obj_type]["a10-name"]

        post_result['post_resp'] = client.post(url, payload)
        post_result['result'] = True

        try:
            need_update = false
            resp = client.get()
            for k,v in tree.items():
               if k in resp:
                    if v != resp[k]:
                        need_update = true
                        break
            if need_update:
                client.put()
                return
        except ae.DNE:
            pass

        client.post()

obj_dicty = {'netmask': '255.255.255.0', 'name': 'VS2', 'a10_name': 'vs2', 'ip_address': '192.168.43.6', 'port_list': [OrderedDict([(22, [OrderedDict([('protocol', 'tcp')])])]), OrderedDict([(80, [OrderedDict([('protocol', 'tcp')])])]), OrderedDict([('service_group', [OrderedDict([('sg1', [OrderedDict([('member_list', [OrderedDict([('mem1', [OrderedDict([('host', '10.7.11.1')])])]), OrderedDict([('mem2', [OrderedDict([('host', '10.7.11.2')])])])])]), OrderedDict([('lb_type', 'round_robin')])])])])])], 'a10_obj': 'slb_virtual_server'}

parse_obj('virtual_server', 'slb', None, **obj_dicty)
