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
AVAILABLE_PROPERTIES = ["backup_server_event_log","conn_rate","conn_rate_duration","conn_rate_grace_period","conn_rate_log","conn_rate_revert_duration","conn_revert_rate","extended_stats","health_check","health_check_disable","l4_session_revert_duration","l4_session_usage","l4_session_usage_duration","l4_session_usage_grace_period","l4_session_usage_log","l4_session_usage_revert_rate","lb_method","lc_method","member_list","min_active_member","min_active_member_action","name","priorities","priority_affinity","protocol","pseudo_round_robin","report_delay","reset","reset_on_server_selection_fail","reset_priority_affinity","rpt_ext_server","sample_rsp_time","sampling_enable","stateless_auto_switch","stateless_lb_method","stateless_lb_method2","stats_data_action","strict_select","template_policy","template_port","template_server","top_fastest","top_slowest","traffic_replication_mirror","traffic_replication_mirror_da_repl","traffic_replication_mirror_ip_repl","traffic_replication_mirror_sa_da_repl","traffic_replication_mirror_sa_repl","user_tag","uuid",]


def new_url():
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/service-group/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)

def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/service-group/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["name"]

    return url_base.format(**f_dict)


def create(**kwargs):
    ret = dict(
        name="a10_slb_service_group",
        changes={},
        original_message="",
        result=False,
        comment=""
    )

    try:
        post_result = __salt__['a10.create']("service-group",
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
        name="a10_slb_service_group",
        changes={},
        original_message="",
        result=False,
        comment=""
    )

    try:
        post_result = __salt__['a10.update']("service-group",
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
        name="a10_slb_service_group",
        changes={},
        original_message="",
        result=False,
        comment=""
    )

    try:
        post_result = __salt__['a10.delete']("service-group",
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