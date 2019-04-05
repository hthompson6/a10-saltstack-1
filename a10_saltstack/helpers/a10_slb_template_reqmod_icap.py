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
    "allowed_http_methods",
    "bypass_ip_cfg",
    "fail_close",
    "include_protocol_in_uri",
    "logging",
    "min_payload_size",
    "a10_name",
    "preview",
    "server_ssl",
    "service_group",
    "service_url",
    "source_ip",
    "tcp_proxy",
    "user_tag",
    "uuid",
]

REF_PROPERTIES = {
    "logging": "/axapi/v3/slb/template/logging",
    "server_ssl": "/axapi/v3/slb/template/server-ssl",
    "service_group": "/axapi/v3/slb/service-group",
    "source_ip": "/axapi/v3/slb/template/persist/source-ip",
    "tcp_proxy": "/axapi/v3/slb/template/tcp-proxy",
}

MODULE_NAME = "reqmod-icap"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/template/reqmod-icap/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/template/reqmod-icap/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["a10-name"]

    return url_base.format(**f_dict)