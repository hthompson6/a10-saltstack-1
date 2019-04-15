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
    "destination_ip_address_list",
    "encap",
    "host_list",
    "id",
    "source_ip_address",
    "user_tag",
    "uuid",
]

REF_PROPERTIES = {
    "destination_ip_address_list": "/axapi/v3/overlay-tunnel/vtep/{id}/destination-ip-address/{ip-address}",
    "host_list": "/axapi/v3/overlay-tunnel/vtep/{id}/host/{ip-addr}+{overlay-mac-addr}+{vni}+{destination-vtep}",
    "source_ip_address": "/axapi/v3/overlay-tunnel/vtep/{id}/source-ip-address",
}

MODULE_NAME = "vtep"

PARENT_KEYS = []

CHILD_KEYS = ["id",]


def new_url():
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/overlay-tunnel/vtep/{id}"
    f_dict = {}
    f_dict["id"] = ""

    return url_base.format(**f_dict)


def existing_url():
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/overlay-tunnel/vtep/{id}"
    f_dict = {}
    f_dict["id"] = kwargs["id"]

    return url_base.format(**f_dict)