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
AVAILABLE_PROPERTIES = ["address_type","ethernet","nat_pool","src_dst","trunk","uuid","value","ve","virtual_server","action_direction","event_number",]

REF_PROPERTIES = {
    "ethernet": "/axapi/v3/interface/ethernet",
    "ve": "/axapi/v3/interface/ve",
    "virtual_server": "/axapi/v3/slb/virtual-server",
}

MODULE_NAME = "mac"

PARENT_KEYS = ["action_direction","event_number",]

CHILD_KEYS = ["src-dst",]


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/sys-ut/event/{event_number}/action/{action_direction}/l2/mac/{src-dst}"
    f_dict = {}
    f_dict["src-dst"] = ""
    f_dict["action_direction"] = kwargs["action_direction"]
    f_dict["event_number"] = kwargs["event_number"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/sys-ut/event/{event_number}/action/{action_direction}/l2/mac/{src-dst}"
    f_dict = {}
    f_dict["src-dst"] = kwargs["src-dst"]
    f_dict["action_direction"] = kwargs["action_direction"]
    f_dict["event_number"] = kwargs["event_number"]

    return url_base.format(**f_dict)