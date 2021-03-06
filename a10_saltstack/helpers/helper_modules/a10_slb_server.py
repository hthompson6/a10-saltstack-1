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
AVAILABLE_PROPERTIES = ["action","alternate_server","conn_limit","conn_resume","extended_stats","external_ip","fqdn_name","health_check","health_check_disable","host","ipv6","name","no_logging","port_list","sampling_enable","server_ipv6_addr","slow_start","spoofing_cache","stats_data_action","template_server","user_tag","uuid","weight",]

REF_PROPERTIES = {
    "health_check": "/axapi/v3/health/monitor",
    "port_list": "/axapi/v3/slb/server/{name}/port/{port-number}+{protocol}",
    "template_server": "/axapi/v3/slb/template/server",
}

MODULE_NAME = "server"

PARENT_KEYS = []

CHILD_KEYS = ["name",]


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/server/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/server/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["name"]

    return url_base.format(**f_dict)