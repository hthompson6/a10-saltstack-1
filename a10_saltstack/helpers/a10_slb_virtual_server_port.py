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
    "acl_id_list",
    "acl_name_list",
    "action",
    "aflex_scripts",
    "alt_protocol1",
    "alt_protocol2",
    "alternate_port",
    "alternate_port_number",
    "auth_cfg",
    "auto",
    "clientip_sticky_nat",
    "conn_limit",
    "def_selection_if_pref_failed",
    "enable_playerid_check",
    "eth_fwd",
    "eth_rev",
    "expand",
    "extended_stats",
    "force_routing_mode",
    "gslb_enable",
    "ha_conn_mirror",
    "ipinip",
    "l7_hardware_assist",
    "message_switching",
    "a10_name",
    "no_auto_up_on_aflex",
    "no_dest_nat",
    "no_logging",
    "on_syn",
    "persist_type",
    "pool",
    "port_number",
    "port_translation",
    "precedence",
    "protocol",
    "range",
    "rate",
    "redirect_to_https",
    "req_fail",
    "reset",
    "reset_on_server_selection_fail",
    "rtp_sip_call_id_match",
    "sampling_enable",
    "scaleout_bucket_count",
    "scaleout_device_group",
    "secs",
    "serv_sel_fail",
    "service_group",
    "skip_rev_hash",
    "snat_on_vip",
    "stats_data_action",
    "syn_cookie",
    "template_cache",
    "template_client_ssl",
    "template_connection_reuse",
    "template_dblb",
    "template_diameter",
    "template_dns",
    "template_dynamic_service",
    "template_external_service",
    "template_file_inspection",
    "template_fix",
    "template_ftp",
    "template_http",
    "template_http_policy",
    "template_imap_pop3",
    "template_persist_cookie",
    "template_persist_destination_ip",
    "template_persist_source_ip",
    "template_persist_ssl_sid",
    "template_policy",
    "template_reqmod_icap",
    "template_respmod_icap",
    "template_scaleout",
    "template_server_ssl",
    "template_sip",
    "template_smpp",
    "template_smtp",
    "template_ssli",
    "template_tcp",
    "template_tcp_proxy",
    "template_tcp_proxy_client",
    "template_tcp_proxy_server",
    "template_udp",
    "template_virtual_port",
    "trunk_fwd",
    "trunk_rev",
    "use_alternate_port",
    "use_cgnv6",
    "use_default_if_no_server",
    "use_rcv_hop_for_resp",
    "user_tag",
    "uuid",
    "view",
    "waf_template",
    "when_down",
    "when_down_protocol2",
    "virtual_server_name",
]

REF_PROPERTIES = [
    "pool",
    "service_group",
    "template_cache",
    "template_client_ssl",
    "template_connection_reuse",
    "template_dblb",
    "template_diameter",
    "template_dns",
    "template_dynamic_service",
    "template_external_service",
    "template_file_inspection",
    "template_fix",
    "template_ftp",
    "template_http",
    "template_http_policy",
    "template_imap_pop3",
    "template_persist_cookie",
    "template_persist_destination_ip",
    "template_persist_source_ip",
    "template_persist_ssl_sid",
    "template_policy",
    "template_reqmod_icap",
    "template_respmod_icap",
    "template_server_ssl",
    "template_sip",
    "template_smpp",
    "template_smtp",
    "template_ssli",
    "template_tcp",
    "template_tcp_proxy",
    "template_tcp_proxy_client",
    "template_tcp_proxy_server",
    "template_udp",
    "template_virtual_port",
    "waf_template",
]

MODULE_NAME = "port"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/virtual-server/{virtual_server_name}/port/{port-number}+{protocol}"
    f_dict = {}
    f_dict["port-number"] = ""
    f_dict["protocol"] = ""
    f_dict["virtual_server_name"] = kwargs["virtual_server_name"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/virtual-server/{virtual_server_name}/port/{port-number}+{protocol}"
    f_dict = {}
    f_dict["port-number"] = kwargs["port-number"]
    f_dict["protocol"] = kwargs["protocol"]
    f_dict["virtual_server_name"] = kwargs["virtual_server_name"]

    return url_base.format(**f_dict)