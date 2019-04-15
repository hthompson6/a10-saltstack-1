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
    "destination_vtep",
    "ip_addr",
    "overlay_mac_addr",
    "uuid",
    "vni",
    "vtep_id",
]

REF_PROPERTIES = {
}

MODULE_NAME = "host"

PARENT_KEYS = ["vtep_id",]

CHILD_KEYS = ["ip-addr","overlay-mac-addr","vni","destination-vtep",]


def new_url():
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/overlay-tunnel/vtep/{vtep_id}/host/{ip-addr}+{overlay-mac-addr}+{vni}+{destination-vtep}"
    f_dict = {}
    f_dict["ip-addr"] = ""
    f_dict["overlay-mac-addr"] = ""
    f_dict["vni"] = ""
    f_dict["destination-vtep"] = ""
    f_dict["vtep_id"] = kwargs["vtep_id"]

    return url_base.format(**f_dict)


def existing_url():
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/overlay-tunnel/vtep/{vtep_id}/host/{ip-addr}+{overlay-mac-addr}+{vni}+{destination-vtep}"
    f_dict = {}
    f_dict["ip-addr"] = kwargs["ip-addr"]
    f_dict["overlay-mac-addr"] = kwargs["overlay-mac-addr"]
    f_dict["vni"] = kwargs["vni"]
    f_dict["destination-vtep"] = kwargs["destination-vtep"]
    f_dict["vtep_id"] = kwargs["vtep_id"]

    return url_base.format(**f_dict)