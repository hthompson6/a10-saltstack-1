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
AVAILABLE_PROPERTIES = ["A10_AX_AUTH_URI","a10_dynamic_defined","attr_int","attr_int_val","attr_ip","attr_ipv4","attr_num","attr_str","attr_str_val","attr_type","attribute_name","custom_attr_str","custom_attr_type","integer_type","ip_type","string_type","uuid",]

MODULE_NAME = 'attribute'

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/aam/authorization/policy/{policy_name}/attribute/{attr-num}"
    f_dict = {}
    f_dict["attr-num"] = ""
    f_dict["policy_name"] = kwargs["policy_name"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/aam/authorization/policy/{policy_name}/attribute/{attr-num}"
    f_dict = {}
    f_dict["attr-num"] = kwargs["attr_num"]
    f_dict["policy_name"] = kwargs["policy_name"]

    return url_base.format(**f_dict)