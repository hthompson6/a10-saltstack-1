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
AVAILABLE_PROPERTIES = [
    "arp",
    "comp_hex",
    "dst",
    "exit",
    "hex",
    "icmp",
    "icmpv6",
    "integer",
    "integer_comp",
    "integer_max",
    "integer_min",
    "ip",
    "ipv4_address",
    "ipv4_netmask",
    "ipv6",
    "ipv6_adddress",
    "l3_proto",
    "length",
    "mac",
    "mac_addr",
    "max_hex",
    "min_hex",
    "neighbor",
    "number",
    "offset",
    "oper_range",
    "port",
    "port_num",
    "port_num_max",
    "port_num_min",
    "prot_num",
    "proto",
    "range",
    "src",
    "tcp",
    "udp",
    "WORD",
    "WORD1",
    "WORD2",
]

REF_PROPERTIES = {
}

MODULE_NAME = "filter-config"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url():
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/axdebug/filter-config"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url():
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/axdebug/filter-config"
    f_dict = {}

    return url_base.format(**f_dict)