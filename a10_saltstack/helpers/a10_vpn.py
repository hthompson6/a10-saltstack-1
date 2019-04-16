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
AVAILABLE_PROPERTIES = ["asymmetric_flow_support","error","fragment_after_encap","ike_gateway_list","ike_sa_timeout","ike_stats_global","ipsec_error_dump","ipsec_list","jumbo_fragment","nat_traversal_flow_affinity","revocation_list","sampling_enable","stateful_mode","tcp_mss_adjust_disable","uuid",]

REF_PROPERTIES = {
    "error": "/axapi/v3/vpn/error",
    "ike_gateway_list": "/axapi/v3/vpn/ike-gateway/{name}",
    "ike_stats_global": "/axapi/v3/vpn/ike-stats-global",
    "ipsec_list": "/axapi/v3/vpn/ipsec/{name}",
    "revocation_list": "/axapi/v3/vpn/revocation/{name}",
}

MODULE_NAME = "vpn"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/vpn"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/vpn"
    f_dict = {}

    return url_base.format(**f_dict)