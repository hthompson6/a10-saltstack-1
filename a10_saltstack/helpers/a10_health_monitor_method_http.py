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
AVAILABLE_PROPERTIES = ["http","http_encrypted","http_expect","http_host","http_kerberos_auth","http_kerberos_kdc","http_kerberos_realm","http_maintenance_code","http_password","http_password_string","http_port","http_postdata","http_postfile","http_response_code","http_text","http_url","http_username","post_path","post_type","response_code_regex","text_regex","url_path","url_type","uuid","monitor_name",]

REF_PROPERTIES = {
}

MODULE_NAME = "http"

PARENT_KEYS = ["monitor_name",]

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/health/monitor/{monitor_name}/method/http"
    f_dict = {}
    f_dict["monitor_name"] = kwargs["monitor_name"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/health/monitor/{monitor_name}/method/http"
    f_dict = {}
    f_dict["monitor_name"] = kwargs["monitor_name"]

    return url_base.format(**f_dict)