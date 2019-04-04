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
    "after_disable",
    "auto_nat_no_ip_refresh",
    "buff_thresh",
    "buff_thresh_hw_buff",
    "buff_thresh_relieve_thresh",
    "buff_thresh_sys_buff_high",
    "buff_thresh_sys_buff_low",
    "compress_block_size",
    "conn_rate_limit",
    "ddos_protection",
    "disable_adaptive_resource_check",
    "disable_server_auto_reselect",
    "dns_cache_age",
    "dns_cache_enable",
    "dns_cache_entry_size",
    "dns_vip_stateless",
    "drop_icmp_to_vip_when_vip_down",
    "dsr_health_check_enable",
    "enable_l7_req_acct",
    "entity",
    "exclude_destination",
    "extended_stats",
    "fast_path_disable",
    "gateway_health_check",
    "graceful_shutdown",
    "graceful_shutdown_enable",
    "honor_server_response_ttl",
    "hw_compression",
    "hw_syn_rr",
    "interval",
    "l2l3_trunk_lb_disable",
    "log_for_reset_unknown_conn",
    "low_latency",
    "max_buff_queued_per_conn",
    "max_http_header_count",
    "max_local_rate",
    "max_remote_rate",
    "msl_time",
    "mss_table",
    "no_auto_up_on_aflex",
    "override_port",
    "pkt_rate_for_reset_unknown_conn",
    "player_id_check_enable",
    "range",
    "range_end",
    "range_start",
    "rate_limit_logging",
    "reset_stale_session",
    "response_type",
    "scale_out",
    "snat_gwy_for_l3",
    "snat_on_vip",
    "software",
    "sort_res",
    "ssli_sni_hash_enable",
    "stateless_sg_multi_binding",
    "stats_data_disable",
    "timeout",
    "ttl_threshold",
    "use_mss_tab",
    "uuid",
]

REF_PROPERTIES = [
    "conn_rate_limit",
]

MODULE_NAME = "common"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/common"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/common"
    f_dict = {}

    return url_base.format(**f_dict)