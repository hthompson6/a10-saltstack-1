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
AVAILABLE_PROPERTIES = ["action_value","bw_per","bw_rate_limit","conn_limit","conn_per","conn_rate_limit","direct_action","direct_action_interval","direct_action_value","direct_fail","direct_logging_drp_rst","direct_pbslb_interval","direct_pbslb_logging","direct_service_group","dns64","interval","lidnum","lockout","log","over_limit_action","request_limit","request_per","request_rate_limit","response_code_rate_limit","user_tag","uuid",]

MODULE_NAME = 'lid'

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/template/policy/{policy_name}/class-list/lid/{lidnum}"
    f_dict = {}
    f_dict["lidnum"] = ""
    f_dict["policy_name"] = module.params["policy_name"]

    return url_base.format(**f_dict)


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/template/policy/{policy_name}/class-list/lid/{lidnum}"
    f_dict = {}
    f_dict["lidnum"] = module.params["lidnum"]
    f_dict["policy_name"] = module.params["policy_name"]

    return url_base.format(**f_dict)