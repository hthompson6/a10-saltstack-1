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
    "admin_preference",
    "auto_detect",
    "auto_map",
    "client_ip",
    "device_name",
    "gateway_ip_addr",
    "health_check_action",
    "ip_address",
    "max_client",
    "proto_aging_fast",
    "proto_aging_time",
    "proto_compatible",
    "rdt_value",
    "user_tag",
    "uuid",
    "vip_server",
    "site_name",
]

REF_PROPERTIES = {
    "vip_server": "/axapi/v3/gslb/site/{site-name}/slb-dev/{device-name}/vip-server",
}

MODULE_NAME = "slb-dev"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/gslb/site/{site_name}/slb-dev/{device-name}"
    f_dict = {}
    f_dict["device-name"] = ""
    f_dict["site_name"] = kwargs["site_name"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/gslb/site/{site_name}/slb-dev/{device-name}"
    f_dict = {}
    f_dict["device-name"] = kwargs["device-name"]
    f_dict["site_name"] = kwargs["site_name"]

    return url_base.format(**f_dict)