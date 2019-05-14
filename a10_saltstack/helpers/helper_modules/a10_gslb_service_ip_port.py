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
AVAILABLE_PROPERTIES = ["action","follow_port_protocol","health_check","health_check_disable","health_check_follow_port","health_check_protocol_disable","port_num","port_proto","sampling_enable","user_tag","uuid","service_ip_node_name",]

REF_PROPERTIES = {
    "health_check": "/axapi/v3/health/monitor",
}

MODULE_NAME = "port"

PARENT_KEYS = ["service_ip_node_name",]

CHILD_KEYS = ["port-num","port-proto",]


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/gslb/service-ip/{service_ip_node_name}/port/{port-num}+{port-proto}"
    f_dict = {}
    f_dict["port-num"] = ""
    f_dict["port-proto"] = ""
    f_dict["service_ip_node_name"] = kwargs["service_ip_node_name"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/gslb/service-ip/{service_ip_node_name}/port/{port-num}+{port-proto}"
    f_dict = {}
    f_dict["port-num"] = kwargs["port-num"]
    f_dict["port-proto"] = kwargs["port-proto"]
    f_dict["service_ip_node_name"] = kwargs["service_ip_node_name"]

    return url_base.format(**f_dict)