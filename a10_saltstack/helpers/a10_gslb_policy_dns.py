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
AVAILABLE_PROPERTIES = [    "action",
    "action_type",
    "active_only",
    "active_only_fail_safe",
    "aging_time",
    "backup_alias",
    "backup_server",
    "block_action",
    "block_type",
    "block_value",
    "cache",
    "cname_detect",
    "delegation",
    "dns_addition_mx",
    "dns_auto_map",
    "dynamic_preference",
    "dynamic_weight",
    "external_ip",
    "external_soa",
    "geoloc_action",
    "geoloc_alias",
    "geoloc_policy",
    "hint",
    "ip_replace",
    "ipv6",
    "logging",
    "proxy_block_port_range_list",
    "selected_only",
    "selected_only_value",
    "server",
    "server_addition_mx",
    "server_any",
    "server_authoritative",
    "server_auto_ns",
    "server_auto_ptr",
    "server_cname",
    "server_full_list",
    "server_mode_only",
    "server_mx",
    "server_naptr",
    "server_ns",
    "server_ns_list",
    "server_ptr",
    "server_sec",
    "server_srv",
    "server_txt",
    "sticky",
    "sticky_aging_time",
    "sticky_ipv6_mask",
    "sticky_mask",
    "template",
    "ttl",
    "use_server_ttl",
    "uuid",
    "policy_name",
]

MODULE_NAME = "dns"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/gslb/policy/{policy_name}/dns"
    f_dict = {}
    f_dict["policy_name"] = kwargs["policy_name"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/gslb/policy/{policy_name}/dns"
    f_dict = {}
    f_dict["policy_name"] = kwargs["policy_name"]

    return url_base.format(**f_dict)