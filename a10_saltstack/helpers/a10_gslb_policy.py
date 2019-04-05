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
    "active_rdt",
    "active_servers_enable",
    "active_servers_fail_break",
    "admin_ip_enable",
    "admin_ip_top_only",
    "admin_preference",
    "alias_admin_preference",
    "amount_first",
    "auto_map",
    "bw_cost_enable",
    "bw_cost_fail_break",
    "capacity",
    "connection_load",
    "dns",
    "edns",
    "geo_location_list",
    "geo_location_match",
    "geographic",
    "health_check",
    "health_check_preference_enable",
    "health_preference_top",
    "ip_list",
    "least_response",
    "metric_fail_break",
    "metric_force_check",
    "metric_order",
    "metric_type",
    "a10_name",
    "num_session_enable",
    "num_session_tolerance",
    "ordered_ip_top_only",
    "round_robin",
    "user_tag",
    "uuid",
    "weighted_alias",
    "weighted_ip_enable",
    "weighted_ip_total_hits",
    "weighted_site_enable",
    "weighted_site_total_hits",
]

REF_PROPERTIES = {
    "active_rdt": "/axapi/v3/gslb/policy/{name}/active-rdt",
    "auto_map": "/axapi/v3/gslb/policy/{name}/auto-map",
    "capacity": "/axapi/v3/gslb/policy/{name}/capacity",
    "connection_load": "/axapi/v3/gslb/policy/{name}/connection-load",
    "dns": "/axapi/v3/gslb/policy/{name}/dns",
    "edns": "/axapi/v3/gslb/policy/{name}/edns",
    "geo_location_list": "/axapi/v3/gslb/policy/{name}/geo-location/{name}",
    "geo_location_match": "/axapi/v3/gslb/policy/{name}/geo-location-match",
    "ip_list": "/axapi/v3/gslb/ip-list",
}

MODULE_NAME = "policy"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/gslb/policy/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/gslb/policy/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["a10-name"]

    return url_base.format(**f_dict)