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
AVAILABLE_PROPERTIES = [    "address_family",
    "adjacency_check",
    "area_password_cfg",
    "authentication",
    "bfd",
    "default_information",
    "distance_list",
    "domain_password_cfg",
    "ha_standby_extra_cost",
    "ignore_lsp_errors",
    "is_type",
    "log_adjacency_changes_cfg",
    "lsp_gen_interval_list",
    "lsp_refresh_interval",
    "max_lsp_lifetime",
    "metric_style_list",
    "net_list",
    "passive_interface_list",
    "protocol_list",
    "redistribute",
    "set_overload_bit_cfg",
    "spf_interval_exp_list",
    "summary_address_list",
    "tag",
    "user_tag",
    "uuid",
]

MODULE_NAME = "isis"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/router/isis/{tag}"
    f_dict = {}
    f_dict["tag"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/router/isis/{tag}"
    f_dict = {}
    f_dict["tag"] = kwargs["tag"]

    return url_base.format(**f_dict)