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
AVAILABLE_PROPERTIES = ["dest_rule_list","dynamic_pool_size","inside_end_address","inside_netmask","inside_start_address","method","nat_end_address","nat_ip_list","nat_netmask","nat_start_address","offset","partition","ports_per_user","respond_to_user_mac","session_quota","usable_nat_ports","uuid","vrid",]

REF_PROPERTIES = {
}

MODULE_NAME = "ipv6address"

PARENT_KEYS = []

CHILD_KEYS = ["inside-start-address","inside-end-address","inside-netmask","partition",]


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/cgnv6/fixed-nat/inside/ipv6address/{inside-start-address}+{inside-end-address}+{inside-netmask}+{partition}"
    f_dict = {}
    f_dict["inside-start-address"] = ""
    f_dict["inside-end-address"] = ""
    f_dict["inside-netmask"] = ""
    f_dict["partition"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/cgnv6/fixed-nat/inside/ipv6address/{inside-start-address}+{inside-end-address}+{inside-netmask}+{partition}"
    f_dict = {}
    f_dict["inside-start-address"] = kwargs["inside-start-address"]
    f_dict["inside-end-address"] = kwargs["inside-end-address"]
    f_dict["inside-netmask"] = kwargs["inside-netmask"]
    f_dict["partition"] = kwargs["partition"]

    return url_base.format(**f_dict)