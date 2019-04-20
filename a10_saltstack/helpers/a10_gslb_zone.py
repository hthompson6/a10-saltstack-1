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
AVAILABLE_PROPERTIES = ["disable","dns_mx_record_list","dns_ns_record_list","dns_soa_record","name","policy","sampling_enable","service_list","template","ttl","use_server_ttl","user_tag","uuid",]

REF_PROPERTIES = {
    "dns_mx_record_list": "/axapi/v3/gslb/zone/{name}/dns-mx-record/{mx-name}",
    "dns_ns_record_list": "/axapi/v3/gslb/zone/{name}/dns-ns-record/{ns-name}",
    "service_list": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}",
}

MODULE_NAME = "zone"

PARENT_KEYS = []

CHILD_KEYS = ["name",]


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/gslb/zone/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/gslb/zone/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["name"]

    return url_base.format(**f_dict)