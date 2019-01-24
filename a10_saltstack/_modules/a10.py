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


try:
    from a10_saltstack import client as a10_client
    from a10_saltstack.kwbl import KW_OUT, translate_blacklist as translateBlacklist
    from a10_saltstack import errors as a10_ex
    from a10_saltstack.helpers import helper as a10_helper
    HAS_A10 = True
except ImportError:
    HAS_A10 = False

import logging
LOG = logging.getLogger(__file__)


__virtualname__ = 'a10'
__proxyenabled__ = ['a10']


def __virtual__():
    if HAS_A10 and 'proxy' in __opts__:
        return __virtualname__
    return (False, 'The a10 module could not be loaded: '
                   'proxy could not be loaded.')


def _get_client(**kwargs):
    return a10_client.A10Client(__proxy__['a10.get_session']())


def _build_envelope(title, data):
    return {
        title: data
    }


def _to_axapi(key):
    return translateBlacklist(key, KW_OUT).replace("_", "-")


def _build_dict_from_param(param):
    rv = {}

    for k,v in param.items():
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


def create(obj_type, **kwargs):
    url = a10_helper.get_url(obj_type, 'create', **kwargs)
    avail_props = a10_helper.get_props(obj_type, **kwargs)
    post_result = {}
    try:
        payload = _build_json(obj_type, avail_props, **kwargs)
        client = _get_client(**kwargs)
        post_result['post_resp'] = client.post(url, payload)
        post_result['result'] = True
    except a10_ex.Exists:
        post_result['result'] = False
    except a10_ex.ACOSException as ex:
        post_result['comment'] = ex.msg
    except Exception as gex:
        raise gex
    return post_result


def update(obj_type, **kwargs):
    url = a10_helper.get_url(obj_type, 'update', **kwargs)
    avail_props = a10_helper.get_props(obj_type, **kwargs)
    post_result = {}
    try:
        payload = _build_json(obj_type, avail_props, **kwargs)
        client = _get_client(**kwargs)
        post_result = client.put(url, payload)
    except a10_ex.Exists:
        post_result['result'] = False
    except a10_ex.ACOSException as ex:
        post_result['comment'] = ex.msg
    except Exception as gex:
        raise gex
    return post_result


def delete(obj_type, **kwargs):
    url = a10_helper.get_url(obj_type, 'delete', **kwargs)
    post_result = {}
    try:
        client = _get_client(**kwargs)
        client.delete(url)
    except a10_ex.Exists:
        post_result['result'] = False
    except a10_ex.ACOSException as ex:
        post_result['comment'] = ex.msg
    except Exception as gex:
        raise gex
    return post_result
