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
AVAILABLE_PROPERTIES = ["community","contact","disable","enable","engineID","group_list","host","location","management_index","slb_data_cache_timeout","SNMPv1_v2c","SNMPv3","user_list","view_list",]

REF_PROPERTIES = {
    "community": "/axapi/v3/snmp-server/community",
    "contact": "/axapi/v3/snmp-server/contact",
    "disable": "/axapi/v3/snmp-server/disable",
    "enable": "/axapi/v3/snmp-server/enable",
    "engineID": "/axapi/v3/snmp-server/engineID",
    "group_list": "/axapi/v3/snmp-server/group/{groupname}",
    "host": "/axapi/v3/snmp-server/host",
    "location": "/axapi/v3/snmp-server/location",
    "management_index": "/axapi/v3/snmp-server/management-index",
    "slb_data_cache_timeout": "/axapi/v3/snmp-server/slb-data-cache-timeout",
    "SNMPv1_v2c": "/axapi/v3/snmp-server/SNMPv1-v2c",
    "SNMPv3": "/axapi/v3/snmp-server/SNMPv3",
    "user_list": "/axapi/v3/snmp-server/user/{username}",
    "view_list": "/axapi/v3/snmp-server/view/{viewname}+{oid}",
}

MODULE_NAME = "snmp-server"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/snmp-server"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/snmp-server"
    f_dict = {}

    return url_base.format(**f_dict)