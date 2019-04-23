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
AVAILABLE_PROPERTIES = ["access_list_list","address","anomaly_drop","as_path_list","community_list","default_gateway","dns","extcommunity_list","frag","icmp","mgmt_traffic_list","nat","nat_global","prefix_list_list","reroute","route","tcp",]

REF_PROPERTIES = {
    "access_list_list": "/axapi/v3/ip/access-list/{name}",
    "address": "/axapi/v3/ip/address",
    "anomaly_drop": "/axapi/v3/ip/anomaly-drop",
    "as_path_list": "/axapi/v3/ip/as-path/{access-list}+{action}+{value}",
    "community_list": "/axapi/v3/ip/community-list",
    "default_gateway": "/axapi/v3/ip/default-gateway",
    "dns": "/axapi/v3/ip/dns",
    "extcommunity_list": "/axapi/v3/ip/extcommunity-list",
    "frag": "/axapi/v3/ip/frag",
    "icmp": "/axapi/v3/ip/icmp",
    "mgmt_traffic_list": "/axapi/v3/ip/mgmt-traffic/{traffic-type}",
    "nat": "/axapi/v3/ip/nat",
    "nat_global": "/axapi/v3/ip/nat-global",
    "prefix_list_list": "/axapi/v3/ip/prefix-list/{name}",
    "reroute": "/axapi/v3/ip/reroute",
    "route": "/axapi/v3/ip/route",
    "tcp": "/axapi/v3/ip/tcp",
}

MODULE_NAME = "ip"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/ip"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/ip"
    f_dict = {}

    return url_base.format(**f_dict)