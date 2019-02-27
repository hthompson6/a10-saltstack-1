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
AVAILABLE_PROPERTIES = [    "cert",
    "disable_sslv2hello",
    "https",
    "https_encrypted",
    "https_expect",
    "https_host",
    "https_kerberos_auth",
    "https_kerberos_kdc",
    "https_kerberos_realm",
    "https_key_encrypted",
    "https_maintenance_code",
    "https_password",
    "https_password_string",
    "https_postdata",
    "https_postfile",
    "https_response_code",
    "https_text",
    "https_url",
    "https_username",
    "key",
    "key_pass_phrase",
    "key_phrase",
    "post_path",
    "post_type",
    "response_code_regex",
    "text_regex",
    "url_path",
    "url_type",
    "uuid",
    "web_port",
    "monitor_name",
]

MODULE_NAME = "https"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/health/monitor/{monitor_name}/method/https"
    f_dict = {}
    f_dict["monitor_name"] = kwargs["monitor_name"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/health/monitor/{monitor_name}/method/https"
    f_dict = {}
    f_dict["monitor_name"] = kwargs["monitor_name"]

    return url_base.format(**f_dict)