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
AVAILABLE_PROPERTIES = ["bfd","cost_cfg","dead_interval_cfg","disable","hello_interval_cfg","mtu_ignore_cfg","neighbor_cfg","network_list","priority_cfg","retransmit_interval_cfg","transmit_delay_cfg","uuid","ve_ifnum",]

REF_PROPERTIES = {
}

MODULE_NAME = "ospf"

PARENT_KEYS = ["ve_ifnum",]

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/interface/ve/{ve_ifnum}/ipv6/ospf"
    f_dict = {}
    f_dict["ve_ifnum"] = kwargs["ve_ifnum"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/interface/ve/{ve_ifnum}/ipv6/ospf"
    f_dict = {}
    f_dict["ve_ifnum"] = kwargs["ve_ifnum"]

    return url_base.format(**f_dict)