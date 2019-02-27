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
AVAILABLE_PROPERTIES = [    "add",
    "bw_rate_limit",
    "bw_rate_limit_duration",
    "bw_rate_limit_no_logging",
    "bw_rate_limit_resume",
    "conn_limit",
    "conn_limit_no_logging",
    "conn_rate_limit",
    "conn_rate_limit_no_logging",
    "decrement",
    "del_session_on_server_down",
    "dest_nat",
    "down_grace_period",
    "down_timer",
    "dscp",
    "dynamic_member_priority",
    "every",
    "extended_stats",
    "health_check",
    "health_check_disable",
    "inband_health_check",
    "initial_slow_start",
    "a10_name",
    "no_ssl",
    "rate_interval",
    "reassign",
    "request_rate_interval",
    "request_rate_limit",
    "request_rate_no_logging",
    "resel_on_reset",
    "reset",
    "resume",
    "retry",
    "slow_start",
    "source_nat",
    "stats_data_action",
    "sub_group",
    "till",
    "times",
    "user_tag",
    "uuid",
    "weight",
]

MODULE_NAME = "port"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/template/port/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/template/port/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["a10-name"]

    return url_base.format(**f_dict)