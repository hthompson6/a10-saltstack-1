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
AVAILABLE_PROPERTIES = ["add_cpu_core","add_port","all_vlan_limit","anomaly_log","attack","attack_log","bandwidth","bfd","class_list_hitcount_enable","cm_update_file_name_ref","control_cpu","cpu_hyper_thread","cpu_load_sharing","data_cpu","ddos_attack","ddos_log","del_port","delete_cpu_core","glid","hardware_forward","icmp","icmp_rate","icmp6","io_cpu","ip_stats","ip6_stats","ipmi","ipmi_service","ipsec","log_cpu_interval","memory","mgmt_port","modify_port","module_ctrl_cpu","ndisc_ra","per_vlan_limit","promiscuous_mode","queuing_buffer","resource_accounting","resource_usage","session","session_reclaim_limit","sockstress_disable","spe_profile","src_ip_hash_enable","tcp","tcp_stats","telemetry_log","template","template_bind","throughput","trunk","trunk_hw_hash","trunk_xaui_hw_hash","uuid","ve_mac_scheme",]

MODULE_NAME = 'system'

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/system"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/system"
    f_dict = {}

    return url_base.format(**f_dict)