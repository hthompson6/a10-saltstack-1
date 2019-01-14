#!/usr/bin/python

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import salt
import salt.config

from a10_saltstack import errors as a10_ex
from a10_saltstack.kwbl import KW_OUT

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")


# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = ["action","alternate_server","conn_limit","conn_resume","extended_stats","external_ip","fqdn_name","health_check","health_check_disable","host","ipv6","name","no_logging","port_list","sampling_enable","server_ipv6_addr","slow_start","spoofing_cache","stats_data_action","template_server","user_tag","uuid","weight",]


def new_url():
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/server/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)

def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/server/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["name"]

    return url_base.format(**f_dict)


def create(**kwargs):
    ret = dict(
        name="a10_slb_server",
        changes={},
        original_message="",
        result=False,
        comment=""
    )

    try:
        post_result = __salt__['a10.create']("server",
                               new_url(),
                               AVAILABLE_PROPERTIES,
                               **kwargs) 
        ret["changes"].update(**post_result)
        ret["result"] = True
    except a10_ex.Exists:
        ret["result"] = False
    except a10_ex.ACOSException as ex:
        ret["comment"] = ex.msg
        return ret
    except Exception as gex:
        raise gex
    return ret


def update(**kwargs):
    ret = dict(
        name="a10_slb_server",
        changes={},
        original_message="",
        result=False,
        comment=""
    )

    try:
        post_result = __salt__['a10.update']("server",
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
        name="a10_slb_server",
        changes={},
        original_message="",
        result=False,
        comment=""
    )

    try:
        post_result = __salt__['a10.delete']("server",
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