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
    "app",
    "application",
    "a10_name",
    "remark",
    "rule_list",
    "rules_by_zone",
    "sampling_enable",
    "session_statistic",
    "tag",
    "track_app_rule_list",
    "user_tag",
    "uuid",
]

REF_PROPERTIES = {
    "app": "/axapi/v3/rule-set/{name}/app",
    "application": "/axapi/v3/rule-set/{name}/application",
    "rule_list": "/axapi/v3/rule-set/{name}/rule/{name}",
    "rules_by_zone": "/axapi/v3/rule-set/{name}/rules-by-zone",
    "tag": "/axapi/v3/rule-set/{name}/tag",
    "track_app_rule_list": "/axapi/v3/rule-set/{name}/track-app-rule-list",
}

MODULE_NAME = "rule-set"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/rule-set/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/rule-set/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["a10-name"]

    return url_base.format(**f_dict)