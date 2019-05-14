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
AVAILABLE_PROPERTIES = ["auth_portal","auth_portal_image","auth_saml_idp","bw_list","cgnv6","debug_monitor","geo_location","guest_file","health_external","health_postfile","local_uri_file","partition","startup_config","threat_intel","web_category",]

REF_PROPERTIES = {
    "auth_portal": "/axapi/v3/delete/auth-portal",
    "auth_portal_image": "/axapi/v3/delete/auth-portal-image",
    "auth_saml_idp": "/axapi/v3/delete/auth-saml-idp",
    "bw_list": "/axapi/v3/delete/bw-list",
    "cgnv6": "/axapi/v3/delete/cgnv6",
    "debug_monitor": "/axapi/v3/delete/debug-monitor",
    "geo_location": "/axapi/v3/delete/geo-location",
    "guest_file": "/axapi/v3/delete/guest-file",
    "health_external": "/axapi/v3/delete/health-external",
    "health_postfile": "/axapi/v3/delete/health-postfile",
    "local_uri_file": "/axapi/v3/delete/local-uri-file",
    "partition": "/axapi/v3/delete/partition",
    "startup_config": "/axapi/v3/delete/startup-config",
    "threat_intel": "/axapi/v3/delete/threat-intel",
    "web_category": "/axapi/v3/delete/web-category",
}

MODULE_NAME = "delete"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/delete"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/delete"
    f_dict = {}

    return url_base.format(**f_dict)