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



# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = [
    "backup_server_event_log",
    "conn_rate",
    "conn_rate_duration",
    "conn_rate_grace_period",
    "conn_rate_log",
    "conn_rate_revert_duration",
    "conn_revert_rate",
    "extended_stats",
    "health_check",
    "health_check_disable",
    "l4_session_revert_duration",
    "l4_session_usage",
    "l4_session_usage_duration",
    "l4_session_usage_grace_period",
    "l4_session_usage_log",
    "l4_session_usage_revert_rate",
    "lb_method",
    "lc_method",
    "member_list",
    "min_active_member",
    "min_active_member_action",
    "a10_name",
    "priorities",
    "priority_affinity",
    "protocol",
    "pseudo_round_robin",
    "report_delay",
    "reset",
    "reset_on_server_selection_fail",
    "reset_priority_affinity",
    "rpt_ext_server",
    "sample_rsp_time",
    "sampling_enable",
    "stateless_auto_switch",
    "stateless_lb_method",
    "stateless_lb_method2",
    "stats_data_action",
    "strict_select",
    "template_policy",
    "template_port",
    "template_server",
    "top_fastest",
    "top_slowest",
    "traffic_replication_mirror",
    "traffic_replication_mirror_da_repl",
    "traffic_replication_mirror_ip_repl",
    "traffic_replication_mirror_sa_da_repl",
    "traffic_replication_mirror_sa_repl",
    "user_tag",
    "uuid",
]

REF_PROPERTIES = [
    "health_check",
    "member_list",
    "reset",
    "template_policy",
    "template_port",
    "template_server",
]

MODULE_NAME = "service-group"

def new_url(**kwargs):
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
    f_dict["name"] = kwargs["a10-name"]

    return url_base.format(**f_dict)