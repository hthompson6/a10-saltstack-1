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
AVAILABLE_PROPERTIES = ["address_list","allow_promiscuous_vip","cache_spoofing_port","client","dhcp","generate_membership_query","helper_address_list","max_resp_time","nat","ospf","query_interval","rip","router","server","slb_partition_redirect","stateful_firewall","ttl_ignore","uuid","trunk_ifnum",]

REF_PROPERTIES = {
    "ospf": "/axapi/v3/interface/trunk/{ifnum}/ip/ospf",
    "rip": "/axapi/v3/interface/trunk/{ifnum}/ip/rip",
    "router": "/axapi/v3/interface/trunk/{ifnum}/ip/router",
    "stateful_firewall": "/axapi/v3/interface/trunk/{ifnum}/ip/stateful-firewall",
}

MODULE_NAME = "ip"

PARENT_KEYS = ["trunk_ifnum",]

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/interface/trunk/{trunk_ifnum}/ip"
    f_dict = {}
    f_dict["trunk_ifnum"] = kwargs["trunk_ifnum"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/interface/trunk/{trunk_ifnum}/ip"
    f_dict = {}
    f_dict["trunk_ifnum"] = kwargs["trunk_ifnum"]

    return url_base.format(**f_dict)