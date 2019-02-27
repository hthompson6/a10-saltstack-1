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
AVAILABLE_PROPERTIES = [    "account",
    "accounting_server",
    "accounting_service_group",
    "auth_sess_mode",
    "cookie_domain",
    "cookie_domain_group",
    "cookie_max_age",
    "forward_logout_disable",
    "local_logging",
    "log",
    "logon",
    "logout_idle_timeout",
    "logout_url",
    "max_session_time",
    "modify_content_security_policy",
    "a10_name",
    "redirect_hostname",
    "relay",
    "saml_idp",
    "saml_sp",
    "server",
    "service_group",
    "ntype",
    "user_tag",
    "uuid",
]

MODULE_NAME = "template"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/aam/authentication/template/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/aam/authentication/template/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["a10-name"]

    return url_base.format(**f_dict)