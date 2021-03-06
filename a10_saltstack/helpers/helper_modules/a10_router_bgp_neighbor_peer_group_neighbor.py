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
AVAILABLE_PROPERTIES = ["activate","advertisement_interval","allowas_in","allowas_in_count","as_origination_interval","collide_established","connect","default_originate","description","disallow_infinite_holdtime","distribute_lists","dont_capability_negotiate","dynamic","ebgp_multihop","ebgp_multihop_hop_count","enforce_multihop","ethernet","inbound","lif","loopback","maximum_prefix","maximum_prefix_thres","neighbor_filter_lists","neighbor_prefix_lists","neighbor_route_map_lists","next_hop_self","override_capability","pass_encrypted","pass_value","passive","peer_group","peer_group_key","peer_group_remote_as","prefix_list_direction","remove_private_as","route_map","route_refresh","send_community_val","shutdown","strict_capability_match","timers_holdtime","timers_keepalive","trunk","tunnel","unsuppress_map","update_source_ip","update_source_ipv6","uuid","ve","weight","bgp_as_number",]

REF_PROPERTIES = {
}

MODULE_NAME = "peer-group-neighbor"

PARENT_KEYS = ["bgp_as_number",]

CHILD_KEYS = ["peer-group",]


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/router/bgp/{bgp_as_number}/neighbor/peer-group-neighbor/{peer-group}"
    f_dict = {}
    f_dict["peer-group"] = ""
    f_dict["bgp_as_number"] = kwargs["bgp_as_number"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/router/bgp/{bgp_as_number}/neighbor/peer-group-neighbor/{peer-group}"
    f_dict = {}
    f_dict["peer-group"] = kwargs["peer-group"]
    f_dict["bgp_as_number"] = kwargs["bgp_as_number"]

    return url_base.format(**f_dict)