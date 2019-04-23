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
AVAILABLE_PROPERTIES = ["active_rdt","dns","geo_location_list","group_list","ip_list_list","policy_list","protocol","service_group_list","service_ip_list","site_list","system","template","zone_list",]

REF_PROPERTIES = {
    "active_rdt": "/axapi/v3/gslb/active-rdt",
    "dns": "/axapi/v3/gslb/dns",
    "geo_location_list": "/axapi/v3/gslb/geo-location/{geo-locn-obj-name}",
    "group_list": "/axapi/v3/gslb/group/{name}",
    "ip_list_list": "/axapi/v3/gslb/ip-list/{gslb-ip-list-obj-name}",
    "policy_list": "/axapi/v3/gslb/policy/{name}",
    "protocol": "/axapi/v3/gslb/protocol",
    "service_group_list": "/axapi/v3/gslb/service-group/{service-group-name}",
    "service_ip_list": "/axapi/v3/gslb/service-ip/{node-name}",
    "site_list": "/axapi/v3/gslb/site/{site-name}",
    "system": "/axapi/v3/gslb/system",
    "template": "/axapi/v3/gslb/template",
    "zone_list": "/axapi/v3/gslb/zone/{name}",
}

MODULE_NAME = "gslb"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/gslb"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/gslb"
    f_dict = {}

    return url_base.format(**f_dict)