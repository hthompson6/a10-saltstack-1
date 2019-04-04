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
    "acl_id",
    "acl_name",
    "arp_disable",
    "description",
    "disable_vip_adv",
    "enable_disable_action",
    "ethernet",
    "extended_stats",
    "ip_address",
    "ipv6_acl",
    "ipv6_address",
    "migrate_vip",
    "a10_name",
    "netmask",
    "port_list",
    "redistribute_route_map",
    "redistribution_flagged",
    "stats_data_action",
    "template_logging",
    "template_policy",
    "template_scaleout",
    "template_virtual_server",
    "use_if_ip",
    "user_tag",
    "uuid",
    "vrid",
]

REF_PROPERTIES = [
    "acl_id",
    "acl_name",
    "ipv6_acl",
    "migrate_vip",
    "port_list",
    "template_logging",
    "template_policy",
    "template_virtual_server",
]

MODULE_NAME = "virtual-server"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/virtual-server/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/virtual-server/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["a10-name"]

    return url_base.format(**f_dict)