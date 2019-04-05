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
    "aflow",
    "allow_syn_otherflags",
    "allow_vip_to_rport_mapping",
    "conn_limit",
    "conn_limit_no_logging",
    "conn_limit_reset",
    "conn_rate_limit",
    "conn_rate_limit_no_logging",
    "conn_rate_limit_reset",
    "drop_unknown_conn",
    "dscp",
    "ignore_tcp_msl",
    "log_options",
    "a10_name",
    "non_syn_initiation",
    "pkt_rate_interval",
    "pkt_rate_limit_reset",
    "pkt_rate_type",
    "rate",
    "rate_interval",
    "reset_l7_on_failover",
    "reset_unknown_conn",
    "snat_msl",
    "snat_port_preserve",
    "user_tag",
    "uuid",
    "when_rr_enable",
]

REF_PROPERTIES = {
}

MODULE_NAME = "virtual-port"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/template/virtual-port/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/template/virtual-port/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["a10-name"]

    return url_base.format(**f_dict)