#!/usr/bin/python

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import salt
import salt.config

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")


# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = ["acl_id","acl_name","arp_disable","description","disable_vip_adv","enable_disable_action","ethernet","extended_stats","ip_address","ipv6_acl","ipv6_address","migrate_vip","name","netmask","port_list","redistribute_route_map","redistribution_flagged","stats_data_action","template_logging","template_policy","template_scaleout","template_virtual_server","use_if_ip","user_tag","uuid","vrid",]


def create(**kwargs):
    ret = dict(
        name=kwargs['a10_obj'],
        changes={},
        original_message="",
        result=False,
        comment=""
    )

    post_result = __salt__['a10.create']("virtual-server",
                           new_url(),
                           AVAILABLE_PROPERTIES,
                           **kwargs) 
    ret["changes"].update(**post_result['post_resp'])
    del post_result['post_resp']
    ret.update(post_result)
    return ret


def update(**kwargs):
    ret = dict(
        name=kwargs['a10_obj'],
        changes={},
        original_message="",
        result=False,
        comment=""
    )

    try:
        post_result = __salt__['a10.update']("virtual-server",
                               existing_url(**kwargs),     
                               AVAILABLE_PROPERTIES,
                               **kwargs)
        ret["changes"].update(**post_result)
        ret["result"] = True
    except a10_ex.ACOSException as ex:
        ret["comment"] = ex.msg
        return ret
    except Exception as gex:
        raise gex
    return ret


def delete(**kwargs):
    ret = dict(
        name="a10_slb_virtual_server",
        changes={},
        original_message="",
        result=False,
        comment=""
    )

    try:
        post_result = __salt__['a10.delete']("virtual-server",
                               existing_url(**kwargs),      
                               **kwargs)
        client.delete(existing_url(**kwargs))
        ret["result"] = True
    except a10_ex.NotFound:
        ret["result"] = False
    except a10_ex.ACOSException as ex:
        ret["comment"] = ex.msg
        return ret
    except Exception as gex:
        raise gex
    return ret
