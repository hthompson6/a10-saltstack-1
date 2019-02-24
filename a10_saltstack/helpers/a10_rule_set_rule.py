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
AVAILABLE_PROPERTIES = ["action","app_list","application_any","cgnv6_fixed_nat_log","cgnv6_log","cgnv6_lsn_lid","cgnv6_lsn_log","cgnv6_policy","dest_list","dst_class_list","dst_ipv4_any","dst_ipv6_any","dst_threat_list","dst_zone","dst_zone_any","forward_listen_on_port","forward_log","fw_log","fwlog","idle_timeout","ip_version","listen_on_port","log","move_rule","name","policy","remark","sampling_enable","service_any","service_list","source_list","src_class_list","src_ipv4_any","src_ipv6_any","src_threat_list","src_zone","src_zone_any","status","track_application","user_tag","uuid",]

MODULE_NAME = rule

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/rule-set/{rule_set_name}/rule/{name}"
    f_dict = {}
    f_dict["name"] = ""
    f_dict["rule_set_name"] = module.params["rule_set_name"]

    return url_base.format(**f_dict)


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/rule-set/{rule_set_name}/rule/{name}"
    f_dict = {}
    f_dict["name"] = module.params["name"]
    f_dict["rule_set_name"] = module.params["rule_set_name"]

    return url_base.format(**f_dict)