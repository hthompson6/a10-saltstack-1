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
AVAILABLE_PROPERTIES = ["check_now","checknow","config_list","info","proxy_server","reset","revert","use_mgmt_port","uuid",]

REF_PROPERTIES = {
    "check_now": "/axapi/v3/automatic-update/check-now",
    "checknow": "/axapi/v3/automatic-update/checknow",
    "config_list": "/axapi/v3/automatic-update/config/{feature-name}",
    "info": "/axapi/v3/automatic-update/info",
    "proxy_server": "/axapi/v3/automatic-update/proxy-server",
    "reset": "/axapi/v3/automatic-update/reset",
    "revert": "/axapi/v3/automatic-update/revert",
}

MODULE_NAME = "automatic-update"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/automatic-update"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/automatic-update"
    f_dict = {}

    return url_base.format(**f_dict)