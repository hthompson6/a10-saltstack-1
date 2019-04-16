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
AVAILABLE_PROPERTIES = ["active_rdt","auto_map","bw_cost","controller","disable","easy_rdt","ip_server_list","limit","multiple_geo_locations","sampling_enable","site_name","slb_dev_list","template","threshold","user_tag","uuid","weight",]

REF_PROPERTIES = {
    "active_rdt": "/axapi/v3/gslb/site/{site-name}/active-rdt",
    "easy_rdt": "/axapi/v3/gslb/site/{site-name}/easy-rdt",
    "ip_server_list": "/axapi/v3/gslb/site/{site-name}/ip-server/{ip-server-name}",
    "slb_dev_list": "/axapi/v3/gslb/site/{site-name}/slb-dev/{device-name}",
}

MODULE_NAME = "site"

PARENT_KEYS = []

CHILD_KEYS = ["site-name",]


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/gslb/site/{site-name}"
    f_dict = {}
    f_dict["site-name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/gslb/site/{site-name}"
    f_dict = {}
    f_dict["site-name"] = kwargs["site-name"]

    return url_base.format(**f_dict)