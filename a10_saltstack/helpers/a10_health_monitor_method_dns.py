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
    "dns",
    "dns_domain",
    "dns_domain_expect",
    "dns_domain_port",
    "dns_domain_recurse",
    "dns_domain_tcp",
    "dns_domain_type",
    "dns_ip_key",
    "dns_ipv4_addr",
    "dns_ipv4_expect",
    "dns_ipv4_port",
    "dns_ipv4_recurse",
    "dns_ipv4_tcp",
    "dns_ipv6_addr",
    "dns_ipv6_expect",
    "dns_ipv6_port",
    "dns_ipv6_recurse",
    "dns_ipv6_tcp",
    "uuid",
    "monitor_name",
]

REF_PROPERTIES = {
}

MODULE_NAME = "dns"

PARENT_KEYS = ["monitor_name",]

CHILD_KEYS = []


def new_url():
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/health/monitor/{monitor_name}/method/dns"
    f_dict = {}
    f_dict["monitor_name"] = kwargs["monitor_name"]

    return url_base.format(**f_dict)


def existing_url():
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/health/monitor/{monitor_name}/method/dns"
    f_dict = {}
    f_dict["monitor_name"] = kwargs["monitor_name"]

    return url_base.format(**f_dict)