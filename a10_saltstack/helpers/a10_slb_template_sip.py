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
AVAILABLE_PROPERTIES = ["acl_id","acl_name_value","alg_dest_nat","alg_source_nat","call_id_persist_disable","client_keep_alive","client_request_header","client_response_header","dialog_aware","drop_when_client_fail","drop_when_server_fail","exclude_translation","failed_client_selection","failed_client_selection_message","failed_server_selection","failed_server_selection_message","insert_client_ip","interval","keep_server_ip_if_match_acl","name","pstn_gw","server_keep_alive","server_request_header","server_response_header","server_selection_per_request","service_group","smp_call_id_rtp_session","timeout","user_tag","uuid",]

MODULE_NAME = sip

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/template/sip/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/template/sip/{name}"
    f_dict = {}
    f_dict["name"] = module.params["name"]

    return url_base.format(**f_dict)