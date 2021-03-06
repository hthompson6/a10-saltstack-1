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
AVAILABLE_PROPERTIES = ["count","shared","to_shared","uuid","v4_address","v6_address","vrid",]

REF_PROPERTIES = {
}

MODULE_NAME = "static-dest-mapping"

PARENT_KEYS = []

CHILD_KEYS = ["v4-address","v6-address",]


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/cgnv6/nat46-stateless/static-dest-mapping/{v4-address}+{v6-address}"
    f_dict = {}
    f_dict["v4-address"] = ""
    f_dict["v6-address"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/cgnv6/nat46-stateless/static-dest-mapping/{v4-address}+{v6-address}"
    f_dict = {}
    f_dict["v4-address"] = kwargs["v4-address"]
    f_dict["v6-address"] = kwargs["v6-address"]

    return url_base.format(**f_dict)