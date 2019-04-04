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
    "area_list",
    "auto_cost_reference_bandwidth",
    "bfd_all_interfaces",
    "default_information",
    "default_metric",
    "distance",
    "distribute_internal_list",
    "distribute_lists",
    "ha_standby_extra_cost",
    "host_list",
    "log_adjacency_changes_cfg",
    "max_concurrent_dd",
    "maximum_area",
    "neighbor_list",
    "network_list",
    "ospf_1",
    "overflow",
    "passive_interface",
    "process_id",
    "redistribute",
    "rfc1583_compatible",
    "router_id",
    "summary_address_list",
    "timers",
    "user_tag",
    "uuid",
]

REF_PROPERTIES = [
    "area-list",
    "default-information",
    "redistribute",
]

MODULE_NAME = "ospf"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/router/ospf/{process-id}"
    f_dict = {}
    f_dict["process-id"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/router/ospf/{process-id}"
    f_dict = {}
    f_dict["process-id"] = kwargs["process-id"]

    return url_base.format(**f_dict)