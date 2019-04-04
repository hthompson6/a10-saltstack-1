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


def parse_obj(a10_obj, op_type, client, **kwargs):
    forest_gen = ForestGen()
    forest_gen.parse_tree(**kwargs)
    for tree in parser.tree_list:
        url = a10_helper.get_url(tree['a10_obj'], op_type, **kwargs)
        avail_props = a10_helper.get_props(tree['a10_obj'], **kwargs)
        obj_type = a10_helper.get_obj_type(tree['a10_obj'])

        # We want to make a client call here and save it's output.
        # This is wher we handle idempotency.
        # Get the object first. See if it has different values.
        # If it does have different values. Then update it.
        # We need to only check on where the get and current intersect
        # Look into using a set for this.

        # We will use (in) to do this. O(1) function with dicts

        post_result = {}
        payload = _build_json(obj_type, avail_props, **kwargs)
        if payload[obj_type].get('a10-name'):
            payload[obj_type]["name"] = payload[obj_type]["a10-name"]
            del payload[obj_type]["a10-name"]
        client = _get_client()
        post_result['post_resp'] = client.post(url, payload)
        post_result['result'] = True

        try:
            need_update = false
            resp = client.get()
            for k,v in tree:
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
