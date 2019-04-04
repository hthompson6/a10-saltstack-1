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
    "ipv4_nat_addr",
    "port_range_list",
    "user_tag",
    "tunnel_address_ipv6_tunnel_addr",
    "binding_table_name",
]

REF_PROPERTIES = [
    "port-range-list",
]

MODULE_NAME = "nat-address"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/cgnv6/lw-4o6/binding-table/{binding_table_name}/tunnel-address/{tunnel_address_ipv6_tunnel_addr}/nat-address/{ipv4-nat-addr}"
    f_dict = {}
    f_dict["ipv4-nat-addr"] = ""
    f_dict["tunnel_address_ipv6_tunnel_addr"] = kwargs["tunnel_address_ipv6_tunnel_addr"]
    f_dict["binding_table_name"] = kwargs["binding_table_name"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/cgnv6/lw-4o6/binding-table/{binding_table_name}/tunnel-address/{tunnel_address_ipv6_tunnel_addr}/nat-address/{ipv4-nat-addr}"
    f_dict = {}
    f_dict["ipv4-nat-addr"] = kwargs["ipv4-nat-addr"]
    f_dict["tunnel_address_ipv6_tunnel_addr"] = kwargs["tunnel_address_ipv6_tunnel_addr"]
    f_dict["binding_table_name"] = kwargs["binding_table_name"]

    return url_base.format(**f_dict)