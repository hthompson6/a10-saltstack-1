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

REF_PROPERTIES = {
    "acl_id": "/axapi/v3/access-list/standard",
    "acl_name": "/axapi/v3/ip/access-list",
    "ipv6_acl": "/axapi/v3/ipv6/access-list",
    "migrate_vip": "/axapi/v3/slb/virtual-server/{name}/migrate-vip",
    "port_list": "/axapi/v3/slb/virtual-server/{name}/port/{port-number}+{protocol}",
    "template_logging": "/axapi/v3/ip/nat/template/logging",
    "template_policy": "/axapi/v3/slb/template/policy",
    "template_virtual_server": "/axapi/v3/slb/template/virtual-server",
}

MODULE_NAME = "virtual-server"

PARENT_KEYS = []

CHILD_KEYS = ["name",]


def new_url():
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/virtual-server/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url():
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/virtual-server/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["a10-name"]

    return url_base.format(**f_dict)