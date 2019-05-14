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
AVAILABLE_PROPERTIES = ["ipv4_neighbor_list","ipv6_neighbor_list","peer_group_neighbor_list","bgp_as_number",]

REF_PROPERTIES = {
    "ipv4_neighbor_list": "/axapi/v3/router/bgp/{as-number}/address-family/ipv6/neighbor/ipv4-neighbor/{neighbor-ipv4}",
    "ipv6_neighbor_list": "/axapi/v3/router/bgp/{as-number}/address-family/ipv6/neighbor/ipv6-neighbor/{neighbor-ipv6}",
    "peer_group_neighbor_list": "/axapi/v3/router/bgp/{as-number}/address-family/ipv6/neighbor/peer-group-neighbor/{peer-group}",
}

MODULE_NAME = "neighbor"

PARENT_KEYS = ["bgp_as_number",]

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/router/bgp/{bgp_as_number}/address-family/ipv6/neighbor"
    f_dict = {}
    f_dict["bgp_as_number"] = kwargs["bgp_as_number"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/router/bgp/{bgp_as_number}/address-family/ipv6/neighbor"
    f_dict = {}
    f_dict["bgp_as_number"] = kwargs["bgp_as_number"]

    return url_base.format(**f_dict)