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
AVAILABLE_PROPERTIES = ["delay","direction","drop","l1","l2","l3","tcp","template","udp","uuid","case_number","name","state_name",]

REF_PROPERTIES = {
    "l1": "/axapi/v3/sys-ut/state/{name}/next-state/{name}/case/{case-number}/action/{direction}/l1",
    "l2": "/axapi/v3/sys-ut/state/{name}/next-state/{name}/case/{case-number}/action/{direction}/l2",
    "l3": "/axapi/v3/sys-ut/state/{name}/next-state/{name}/case/{case-number}/action/{direction}/l3",
    "tcp": "/axapi/v3/sys-ut/state/{name}/next-state/{name}/case/{case-number}/action/{direction}/tcp",
    "template": "/axapi/v3/sys-ut/template",
    "udp": "/axapi/v3/sys-ut/state/{name}/next-state/{name}/case/{case-number}/action/{direction}/udp",
}

MODULE_NAME = "action"

PARENT_KEYS = ["case_number","name","state_name",]

CHILD_KEYS = ["direction",]


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/sys-ut/state/{state_name}/next-state/{name}/case/{case_number}/action/{direction}"
    f_dict = {}
    f_dict["direction"] = ""
    f_dict["case_number"] = kwargs["case_number"]
    f_dict["name"] = kwargs["name"]
    f_dict["state_name"] = kwargs["state_name"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/sys-ut/state/{state_name}/next-state/{name}/case/{case_number}/action/{direction}"
    f_dict = {}
    f_dict["direction"] = kwargs["direction"]
    f_dict["case_number"] = kwargs["case_number"]
    f_dict["name"] = kwargs["name"]
    f_dict["state_name"] = kwargs["state_name"]

    return url_base.format(**f_dict)