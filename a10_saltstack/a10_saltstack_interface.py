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


from a10_saltstack.client.kwbl import KW_OUT, translate_blacklist as translateBlacklist
from a10_saltstack.client import errors as a10_ex
from a10_saltstack.forest.forestgen import ForestGen
from a10_saltstack.forest.nodes import RootNode, ObjNode, InterNode
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


def _strip_parent(obj):
    del obj['parent-index']
    del obj['parent-key']

    return obj


def _add_root(obj_list):
    root_dict = obj_list[0]
    ref = root_dict['$ref']
    id = root_dict['a10_name']

    del root_dict['$ref']
    del root_dict['a10_name']
    del root_dict['parent-index']

    return RootNode(id, ref, **root_dict)


def _objlist_to_tree(obj_list):
    node_list = []

    root = _add_root(obj_list)
    node_list.append(root)

    del obj_list[0]

    for obj in obj_list:
        if obj.get('parent-key') and obj.get('$ref'):
            inNode = InterNode(obj['parent-key'], obj['$ref'])
            inNode.addParent(node_list[obj['parent-index']])
            node_list.append(inNode)

        for k,v in obj.items():
            if type(v) is dict:
                parent_index = v['parent-index']
                v = _strip_parent(v)
                tempNode = ObjNode(k, **v)
                tempNode.addParent(node_list[parent_index])
                node_list.append(tempNode)

    return root


def parse_obj(a10_obj, op_type, client, **kwargs):
    forest_gen = ForestGen()
    tree_list = forest_gen.parse_tree(a10_obj, kwargs)

    root = _objlist_to_tree(tree_list)

    for tree in parser.tree_list:
        url = a10_helper.get_url(tree['a10_obj'], op_type, **kwargs)
        avail_props = a10_helper.get_props(tree['a10_obj'], **kwargs)
        obj_type = a10_helper.get_obj_type(tree['a10_obj'])

        # We want to make a client call here and save it's output.
        # This is where we handle idempotency.
        # Get the object first. See if it has different values.
        # If it does have different values. Then update it.
        # We need to only check on where the get and current intersect
        # Look into using a set for this.
        #
        # We will use (in) to do this. O(1) function with dicts

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
