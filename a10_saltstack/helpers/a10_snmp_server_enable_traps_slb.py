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
AVAILABLE_PROPERTIES = [    "all",
    "application_buffer_limit",
    "bw_rate_limit_exceed",
    "bw_rate_limit_resume",
    "gateway_down",
    "gateway_up",
    "server_conn_limit",
    "server_conn_resume",
    "server_disabled",
    "server_down",
    "server_selection_failure",
    "server_up",
    "service_conn_limit",
    "service_conn_resume",
    "service_down",
    "service_group_down",
    "service_group_member_down",
    "service_group_member_up",
    "service_group_up",
    "service_up",
    "uuid",
    "vip_connlimit",
    "vip_connratelimit",
    "vip_down",
    "vip_port_connlimit",
    "vip_port_connratelimit",
    "vip_port_down",
    "vip_port_up",
    "vip_up",
]

MODULE_NAME = "slb"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/snmp-server/enable/traps/slb"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/snmp-server/enable/traps/slb"
    f_dict = {}

    return url_base.format(**f_dict)