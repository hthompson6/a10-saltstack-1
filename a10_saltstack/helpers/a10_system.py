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

REF_PROPERTIES = {
    "add_cpu_core": "/axapi/v3/system/add-cpu-core",
    "add_port": "/axapi/v3/system/add-port",
    "all_vlan_limit": "/axapi/v3/system/all-vlan-limit",
    "bandwidth": "/axapi/v3/system/bandwidth",
    "bfd": "/axapi/v3/system/bfd",
    "cm_update_file_name_ref": "/axapi/v3/system/cm-update-file-name-ref",
    "control_cpu": "/axapi/v3/system/control-cpu",
    "cpu_hyper_thread": "/axapi/v3/system/cpu-hyper-thread",
    "cpu_load_sharing": "/axapi/v3/system/cpu-load-sharing",
    "data_cpu": "/axapi/v3/system/data-cpu",
    "del_port": "/axapi/v3/system/del-port",
    "delete_cpu_core": "/axapi/v3/system/delete-cpu-core",
    "glid": "/axapi/v3/glid",
    "hardware_forward": "/axapi/v3/system/hardware-forward",
    "icmp": "/axapi/v3/system/icmp",
    "icmp_rate": "/axapi/v3/system/icmp-rate",
    "icmp6": "/axapi/v3/system/icmp6",
    "io_cpu": "/axapi/v3/system/io-cpu",
    "ip_stats": "/axapi/v3/system/ip-stats",
    "ip6_stats": "/axapi/v3/system/ip6-stats",
    "ipmi": "/axapi/v3/system/ipmi",
    "ipmi_service": "/axapi/v3/system/ipmi-service",
    "ipsec": "/axapi/v3/system/ipsec",
    "memory": "/axapi/v3/system/memory",
    "mgmt_port": "/axapi/v3/system/mgmt-port",
    "modify_port": "/axapi/v3/system/modify-port",
    "ndisc_ra": "/axapi/v3/system/ndisc-ra",
    "per_vlan_limit": "/axapi/v3/system/per-vlan-limit",
    "queuing_buffer": "/axapi/v3/system/queuing-buffer",
    "resource_accounting": "/axapi/v3/system/resource-accounting",
    "resource_usage": "/axapi/v3/system/resource-usage",
    "session": "/axapi/v3/system/session",
    "session_reclaim_limit": "/axapi/v3/system/session-reclaim-limit",
    "spe_profile": "/axapi/v3/system/spe-profile",
    "tcp": "/axapi/v3/system/tcp",
    "tcp_stats": "/axapi/v3/system/tcp-stats",
    "telemetry_log": "/axapi/v3/system/telemetry-log",
    "template": "/axapi/v3/system/template",
    "template_bind": "/axapi/v3/system/template-bind",
    "throughput": "/axapi/v3/system/throughput",
    "trunk": "/axapi/v3/system/trunk",
    "trunk_hw_hash": "/axapi/v3/system/trunk-hw-hash",
    "trunk_xaui_hw_hash": "/axapi/v3/system/trunk-xaui-hw-hash",
    "ve_mac_scheme": "/axapi/v3/system/ve-mac-scheme",
}

MODULE_NAME = "system"

PARENT_KEYS = []

CHILD_KEYS = []


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