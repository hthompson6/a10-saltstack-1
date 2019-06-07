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
AVAILABLE_PROPERTIES = ["cookie_list","destination_ip_list","source_ip_list","ssl_sid_list",]

REF_PROPERTIES = {
    "cookie_list": "/axapi/v3/slb/template/persist/cookie/{name}",
    "destination_ip_list": "/axapi/v3/slb/template/persist/destination-ip/{name}",
    "source_ip_list": "/axapi/v3/slb/template/persist/source-ip/{name}",
    "ssl_sid_list": "/axapi/v3/slb/template/persist/ssl-sid/{name}",
}

MODULE_NAME = "persist"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/template/persist"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/template/persist"
    f_dict = {}

    return url_base.format(**f_dict)