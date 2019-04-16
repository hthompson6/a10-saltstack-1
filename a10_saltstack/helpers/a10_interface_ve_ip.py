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
AVAILABLE_PROPERTIES = ["address_list","allow_promiscuous_vip","client","dhcp","generate_membership_query","helper_address_list","inside","max_resp_time","ospf","outside","query_interval","rip","router","server","slb_partition_redirect","stateful_firewall","ttl_ignore","uuid","ve_ifnum",]

REF_PROPERTIES = {
    "ospf": "/axapi/v3/interface/ve/{ifnum}/ip/ospf",
    "rip": "/axapi/v3/interface/ve/{ifnum}/ip/rip",
    "router": "/axapi/v3/interface/ve/{ifnum}/ip/router",
    "stateful_firewall": "/axapi/v3/interface/ve/{ifnum}/ip/stateful-firewall",
}

MODULE_NAME = "ip"

PARENT_KEYS = ["ve_ifnum",]

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/interface/ve/{ve_ifnum}/ip"
    f_dict = {}
    f_dict["ve_ifnum"] = kwargs["ve_ifnum"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/interface/ve/{ve_ifnum}/ip"
    f_dict = {}
    f_dict["ve_ifnum"] = kwargs["ve_ifnum"]

    return url_base.format(**f_dict)