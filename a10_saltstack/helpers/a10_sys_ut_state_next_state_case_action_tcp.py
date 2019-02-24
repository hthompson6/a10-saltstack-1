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
AVAILABLE_PROPERTIES = ["ack_seq_number","checksum","dest_port","dest_port_value","flags","nat_pool","options","seq_number","src_port","urgent","uuid","window",]

MODULE_NAME = 'tcp'

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/sys-ut/state/{state_name}/next-state/{name}/case/{case_number}/action/{action_direction}/tcp"
    f_dict = {}
    f_dict["action_direction"] = module.params["action_direction"]
    f_dict["case_number"] = module.params["case_number"]
    f_dict["name"] = module.params["name"]
    f_dict["state_name"] = module.params["state_name"]

    return url_base.format(**f_dict)


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/sys-ut/state/{state_name}/next-state/{name}/case/{case_number}/action/{action_direction}/tcp"
    f_dict = {}
    f_dict["action_direction"] = module.params["action_direction"]
    f_dict["case_number"] = module.params["case_number"]
    f_dict["name"] = module.params["name"]
    f_dict["state_name"] = module.params["state_name"]

    return url_base.format(**f_dict)