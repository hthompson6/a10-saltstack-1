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
AVAILABLE_PROPERTIES = ["arp","arp_timeout","bfd","bpdu_fwd_group_list","bridge_vlan_group_list","icmp_rate_limit","icmpv6_rate_limit","lacp","lacp_passthrough_list","lldp","mac_address","mac_age_time","ve_stats","vlan_global","vlan_list",]

REF_PROPERTIES = {
    "arp": "/axapi/v3/network/arp",
    "arp_timeout": "/axapi/v3/network/arp-timeout",
    "bfd": "/axapi/v3/network/bfd",
    "bpdu_fwd_group_list": "/axapi/v3/network/bpdu-fwd-group/{bpdu-fwd-group-number}",
    "bridge_vlan_group_list": "/axapi/v3/network/bridge-vlan-group/{bridge-vlan-group-number}",
    "icmp_rate_limit": "/axapi/v3/network/icmp-rate-limit",
    "icmpv6_rate_limit": "/axapi/v3/network/icmpv6-rate-limit",
    "lacp": "/axapi/v3/network/lacp",
    "lacp_passthrough_list": "/axapi/v3/network/lacp-passthrough/{peer-from}+{peer-to}",
    "lldp": "/axapi/v3/network/lldp",
    "mac_address": "/axapi/v3/network/mac-address",
    "mac_age_time": "/axapi/v3/network/mac-age-time",
    "ve_stats": "/axapi/v3/network/ve-stats",
    "vlan_global": "/axapi/v3/network/vlan-global",
    "vlan_list": "/axapi/v3/network/vlan/{vlan-num}",
}

MODULE_NAME = "network"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/network"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/network"
    f_dict = {}

    return url_base.format(**f_dict)