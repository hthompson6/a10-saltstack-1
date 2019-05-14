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
AVAILABLE_PROPERTIES = ["ddos_protection","dns64","dns64_virtualserver_list","ds_lite","ecmp","fixed_nat","global","http_alg","icmp","l4","logging","lsn","lsn_lid_list","lsn_radius_profile_list","lsn_rule_list_list","lw_4o6","map","nat","nat46_stateless","nat64","nptv6","one_to_one","pcp","port_batch_v1","port_list_list","resource_usage","sctp","server_list","service_group_list","sixrd","stateful_firewall","template","translation",]

REF_PROPERTIES = {
    "ddos_protection": "/axapi/v3/cgnv6/ddos-protection",
    "dns64": "/axapi/v3/cgnv6/dns64",
    "dns64_virtualserver_list": "/axapi/v3/cgnv6/dns64-virtualserver/{name}",
    "ds_lite": "/axapi/v3/cgnv6/ds-lite",
    "ecmp": "/axapi/v3/cgnv6/ecmp",
    "fixed_nat": "/axapi/v3/cgnv6/fixed-nat",
    "global": "/axapi/v3/cgnv6/global",
    "http_alg": "/axapi/v3/cgnv6/http-alg",
    "icmp": "/axapi/v3/cgnv6/icmp",
    "l4": "/axapi/v3/cgnv6/l4",
    "logging": "/axapi/v3/cgnv6/logging",
    "lsn": "/axapi/v3/cgnv6/lsn",
    "lsn_lid_list": "/axapi/v3/cgnv6/lsn-lid/{lid-number}",
    "lsn_radius_profile_list": "/axapi/v3/cgnv6/lsn-radius-profile/{lid-profile-index}",
    "lsn_rule_list_list": "/axapi/v3/cgnv6/lsn-rule-list/{name}",
    "lw_4o6": "/axapi/v3/cgnv6/lw-4o6",
    "map": "/axapi/v3/cgnv6/map",
    "nat": "/axapi/v3/cgnv6/nat",
    "nat46_stateless": "/axapi/v3/cgnv6/nat46-stateless",
    "nat64": "/axapi/v3/cgnv6/nat64",
    "nptv6": "/axapi/v3/cgnv6/nptv6",
    "one_to_one": "/axapi/v3/cgnv6/one-to-one",
    "pcp": "/axapi/v3/cgnv6/pcp",
    "port_batch_v1": "/axapi/v3/cgnv6/port-batch-v1",
    "port_list_list": "/axapi/v3/cgnv6/port-list/{name}",
    "resource_usage": "/axapi/v3/cgnv6/resource-usage",
    "sctp": "/axapi/v3/cgnv6/sctp",
    "server_list": "/axapi/v3/cgnv6/server/{name}",
    "service_group_list": "/axapi/v3/cgnv6/service-group/{name}",
    "sixrd": "/axapi/v3/cgnv6/sixrd",
    "stateful_firewall": "/axapi/v3/cgnv6/stateful-firewall",
    "template": "/axapi/v3/cgnv6/template",
    "translation": "/axapi/v3/cgnv6/translation",
}

MODULE_NAME = "cgnv6"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/cgnv6"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/cgnv6"
    f_dict = {}

    return url_base.format(**f_dict)