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
    "action",
    "external_ip",
    "health_check",
    "health_check_disable",
    "health_check_protocol_disable",
    "ip_address",
    "ipv6",
    "ipv6_address",
    "node_name",
    "port_list",
    "sampling_enable",
    "user_tag",
    "uuid",
]

REF_PROPERTIES = {
    "health_check": "/axapi/v3/health/monitor",
    "port_list": "/axapi/v3/gslb/service-ip/{node-name}/port/{port-num}+{port-proto}",
}

MODULE_NAME = "service-ip"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/gslb/service-ip/{node-name}"
    f_dict = {}
    f_dict["node-name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/gslb/service-ip/{node-name}"
    f_dict = {}
    f_dict["node-name"] = kwargs["node-name"]

    return url_base.format(**f_dict)