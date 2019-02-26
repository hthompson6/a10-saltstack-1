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
AVAILABLE_PROPERTIES = ["access_list","action","auto_neg_enable","bfd","cpu_process","cpu_process_dir","ddos","duplexity","fec_forced_off","fec_forced_on","flow_control","icmp_rate_limit","icmpv6_rate_limit","ifnum","ip","ipv6","isis","l3_vlan_fwd_disable","lldp","load_interval","lw_4o6","map","media_type_copper","monitor_list","mtu","name","nptv6","remove_vlan_tag","sampling_enable","speed","speed_forced_40g","traffic_distribution_mode","trap_source","trunk_group_list","user_tag","uuid",]

MODULE_NAME = 'ethernet'

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/interface/ethernet/{ifnum}"
    f_dict = {}
    f_dict["ifnum"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/interface/ethernet/{ifnum}"
    f_dict = {}
    f_dict["ifnum"] = kwargs["ifnum"]

    return url_base.format(**f_dict)