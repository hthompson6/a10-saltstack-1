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
AVAILABLE_PROPERTIES = [    "action_uri",
    "cookie",
    "domain_variable",
    "match_type",
    "max_packet_collect_size",
    "other_variables",
    "password_variable",
    "uri",
    "user_tag",
    "user_variable",
    "uuid",
    "instance_name",
]

MODULE_NAME = "request-uri"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/aam/authentication/relay/form-based/instance/{instance_name}/request-uri/{match-type}+{uri}"
    f_dict = {}
    f_dict["match-type"] = ""
    f_dict["uri"] = ""
    f_dict["instance_name"] = kwargs["instance_name"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/aam/authentication/relay/form-based/instance/{instance_name}/request-uri/{match-type}+{uri}"
    f_dict = {}
    f_dict["match-type"] = kwargs["match-type"]
    f_dict["uri"] = kwargs["uri"]
    f_dict["instance_name"] = kwargs["instance_name"]

    return url_base.format(**f_dict)