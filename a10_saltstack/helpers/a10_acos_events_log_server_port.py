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
    "health_check",
    "health_check_disable",
    "port_number",
    "protocol",
    "sampling_enable",
    "user_tag",
    "uuid",
    "log_server_name",
]

REF_PROPERTIES = {
    "health_check": "/axapi/v3/health/monitor",
}

MODULE_NAME = "port"

PARENT_KEYS = ["log_server_name",]

CHILD_KEYS = ["port-number","protocol",]


def new_url():
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/acos-events/log-server/{log_server_name}/port/{port-number}+{protocol}"
    f_dict = {}
    f_dict["port-number"] = ""
    f_dict["protocol"] = ""
    f_dict["log_server_name"] = kwargs["log_server_name"]

    return url_base.format(**f_dict)


def existing_url():
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/acos-events/log-server/{log_server_name}/port/{port-number}+{protocol}"
    f_dict = {}
    f_dict["port-number"] = kwargs["port-number"]
    f_dict["protocol"] = kwargs["protocol"]
    f_dict["log_server_name"] = kwargs["log_server_name"]

    return url_base.format(**f_dict)