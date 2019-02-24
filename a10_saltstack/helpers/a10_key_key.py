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
AVAILABLE_PROPERTIES = ["key_number","key_string","user_tag","uuid",]

MODULE_NAME = 'key'

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/key/{key_chain_flag}+{key-chain-name}/key/{key-number}"
    f_dict = {}
    f_dict["key-number"] = ""
    f_dict["key-chain-name"] = module.params["key-chain-name"]
    f_dict["key_chain_flag"] = module.params["key_chain_flag"]

    return url_base.format(**f_dict)


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/key/{key_chain_flag}+{key-chain-name}/key/{key-number}"
    f_dict = {}
    f_dict["key-number"] = module.params["key-number"]
    f_dict["key-chain-name"] = module.params["key-chain-name"]
    f_dict["key_chain_flag"] = module.params["key_chain_flag"]

    return url_base.format(**f_dict)