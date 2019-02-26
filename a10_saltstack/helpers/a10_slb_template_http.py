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
AVAILABLE_PROPERTIES = ["http_100_cont_wait_for_req_complete","bypass_sg","client_ip_hdr_replace","client_port_hdr_replace","compression_auto_disable_on_high_cpu","compression_content_type","compression_enable","compression_exclude_content_type","compression_exclude_uri","compression_keep_accept_encoding","compression_keep_accept_encoding_enable","compression_level","compression_minimum_content_length","cookie_format","failover_url","host_switching","insert_client_ip","insert_client_ip_header_name","insert_client_port","insert_client_port_header_name","keep_client_alive","log_retry","name","non_http_bypass","persist_on_401","rd_port","rd_resp_code","rd_secure","rd_simple_loc","redirect","redirect_rewrite","req_hdr_wait_time","req_hdr_wait_time_val","request_header_erase_list","request_header_insert_list","request_line_case_insensitive","response_content_replace_list","response_header_erase_list","response_header_insert_list","retry_on_5xx","retry_on_5xx_per_req","retry_on_5xx_per_req_val","retry_on_5xx_val","strict_transaction_switch","template","term_11client_hdr_conn_close","url_hash_first","url_hash_last","url_hash_offset","url_hash_persist","url_switching","use_server_status","user_tag","uuid",]

MODULE_NAME = 'http'

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/template/http/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/template/http/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["name"]

    return url_base.format(**f_dict)