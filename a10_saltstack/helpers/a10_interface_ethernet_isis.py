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
AVAILABLE_PROPERTIES = [    "authentication",
    "bfd_cfg",
    "circuit_type",
    "csnp_interval_list",
    "hello_interval_list",
    "hello_interval_minimal_list",
    "hello_multiplier_list",
    "lsp_interval",
    "mesh_group",
    "metric_list",
    "network",
    "padding",
    "password_list",
    "priority_list",
    "retransmit_interval",
    "uuid",
    "wide_metric_list",
    "ethernet_ifnum",
]

MODULE_NAME = "isis"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/interface/ethernet/{ethernet_ifnum}/isis"
    f_dict = {}
    f_dict["ethernet_ifnum"] = kwargs["ethernet_ifnum"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/interface/ethernet/{ethernet_ifnum}/isis"
    f_dict = {}
    f_dict["ethernet_ifnum"] = kwargs["ethernet_ifnum"]

    return url_base.format(**f_dict)