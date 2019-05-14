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
AVAILABLE_PROPERTIES = ["activate","allowas_in","allowas_in_count","default_originate","distribute_lists","inbound","maximum_prefix","maximum_prefix_thres","neighbor_filter_lists","neighbor_ipv4","neighbor_prefix_lists","neighbor_route_map_lists","next_hop_self","peer_group_name","prefix_list_direction","remove_private_as","route_map","send_community_val","unsuppress_map","uuid","weight","bgp_as_number",]

REF_PROPERTIES = {
}

MODULE_NAME = "ipv4-neighbor"

PARENT_KEYS = ["bgp_as_number",]

CHILD_KEYS = ["neighbor-ipv4",]


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/router/bgp/{bgp_as_number}/address-family/ipv6/neighbor/ipv4-neighbor/{neighbor-ipv4}"
    f_dict = {}
    f_dict["neighbor-ipv4"] = ""
    f_dict["bgp_as_number"] = kwargs["bgp_as_number"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/router/bgp/{bgp_as_number}/address-family/ipv6/neighbor/ipv4-neighbor/{neighbor-ipv4}"
    f_dict = {}
    f_dict["neighbor-ipv4"] = kwargs["neighbor-ipv4"]
    f_dict["bgp_as_number"] = kwargs["bgp_as_number"]

    return url_base.format(**f_dict)