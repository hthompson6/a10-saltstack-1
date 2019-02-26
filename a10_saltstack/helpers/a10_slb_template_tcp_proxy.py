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
AVAILABLE_PROPERTIES = ["ack_aggressiveness","alive_if_active","backend_wscale","del_session_on_server_down","disable","disable_sack","disable_tcp_timestamps","disable_window_scale","down","dynamic_buffer_allocation","fin_timeout","force_delete_timeout","force_delete_timeout_100ms","half_close_idle_timeout","half_open_idle_timeout","idle_timeout","init_cwnd","initial_window_size","insert_client_ip","invalid_rate_limit","keepalive_interval","keepalive_probes","mss","nagle","name","qos","receive_buffer","reno","reset_fwd","reset_rev","retransmit_retries","server_down_action","syn_retries","timewait","transmit_buffer","user_tag","uuid",]

MODULE_NAME = 'tcp-proxy'

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/template/tcp-proxy/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/template/tcp-proxy/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["name"]

    return url_base.format(**f_dict)