# Import Python libraries
from __future__ import absolute_import, print_function, unicode_literals

__virtualname__ = 'a10'
__proxyenabled__ = ['a10']


try:
    from a10_saltstack import client as a10_client
    from a10_saltstack.kwbl import KW_IN, KW_OUT, translate_blacklist as translateBlacklist
    from a10_saltstack import errors as a10_ex
    HAS_A10 = True
except ImportError:
    HAS_A10 = False

import logging

LOG = logging.getLogger(__file__)

def __virtual__():
    '''
    We need the Junos adapter libraries for this
    module to work.  We also need a proxymodule entry in __opts__
    in the opts dictionary
    '''
    if HAS_A10 and 'proxy' in __opts__:
        return __virtualname__
    else:
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


def create(obj_type, url, avail_props, **kwargs):
    avail_props = ["acl_id","acl_name","arp_disable","description","disable_vip_adv","enable_disable_action","ethernet","extended_stats","ip_address","ipv6_acl","ipv6_address","migrate_vip","name","netmask","port_list","redistribute_route_map","redistribution_flagged","stats_data_action","template_logging","template_policy","template_scaleout","template_virtual_server","use_if_ip","user_tag","uuid","vrid",]
    payload = _build_json(obj_type, avail_props, **kwargs)
    client = _get_client(**kwargs)
    LOG.debug("================PAYLOAD BELOW===========")
    LOG.debug(payload)
    post_result = client.post(url, payload)
    return post_result


def update(obj_type, url, avail_props, **kwargs):
    payload = _build_json(obj_type, avail_props, **kwargs)
    try:
        client = _get_client(**kwargs)
        post_result = client.put(url, payload)
        ret["changes"].update(**post_result)
        ret["result"] = True
    except a10_ex.ACOSException as ex:
        ret["comment"] = ex.msg
        return ret
    except Exception as gex:
        raise gex
    return ret


def delete(url, **kwargs):
    try:
        client = _get_client(**kwargs)
        client.delete(url)
        ret["result"] = True
    except a10_ex.NotFound:
        ret["result"] = False
    except a10_ex.ACOSException as ex:
        ret["comment"] = ex.msg
        return ret
    except Exception as gex:
        raise gex
    return ret
