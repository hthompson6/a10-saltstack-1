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
    "background",
    "cfm_pwd_cfg",
    "change_text",
    "change_url",
    "confirm_password_var",
    "continue_text",
    "continue_url",
    "new_password_var",
    "new_pwd_cfg",
    "old_password_var",
    "old_pwd_cfg",
    "username_cfg",
    "username_var",
    "uuid",
    "portal_name",
]

REF_PROPERTIES = [
]

MODULE_NAME = "notify-change-password"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/aam/authentication/portal/{portal_name}/notify-change-password"
    f_dict = {}
    f_dict["portal_name"] = kwargs["portal_name"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/aam/authentication/portal/{portal_name}/notify-change-password"
    f_dict = {}
    f_dict["portal_name"] = kwargs["portal_name"]

    return url_base.format(**f_dict)