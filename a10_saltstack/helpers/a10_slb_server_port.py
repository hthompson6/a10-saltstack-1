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
AVAILABLE_PROPERTIES = [    "action",
    "alternate_port",
    "auth_cfg",
    "conn_limit",
    "conn_resume",
    "extended_stats",
    "follow_port_protocol",
    "health_check",
    "health_check_disable",
    "health_check_follow_port",
    "no_logging",
    "no_ssl",
    "port_number",
    "protocol",
    "range",
    "sampling_enable",
    "stats_data_action",
    "template_port",
    "template_server_ssl",
    "user_tag",
    "uuid",
    "weight",
    "server_name",
]

MODULE_NAME = "port"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/server/{server_name}/port/{port-number}+{protocol}"
    f_dict = {}
    f_dict["port-number"] = ""
    f_dict["protocol"] = ""
    f_dict["server_name"] = kwargs["server_name"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/server/{server_name}/port/{port-number}+{protocol}"
    f_dict = {}
    f_dict["port-number"] = kwargs["port-number"]
    f_dict["protocol"] = kwargs["protocol"]
    f_dict["server_name"] = kwargs["server_name"]

    return url_base.format(**f_dict)