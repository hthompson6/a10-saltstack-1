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
AVAILABLE_PROPERTIES = ["alg","endpoint_independent_filtering","endpoint_independent_mapping","global","health_check_gateway_list","inside","performance","port_overloading","port_reservation_list","radius","stun_timeout","tcp",]

REF_PROPERTIES = {
    "alg": "/axapi/v3/cgnv6/lsn/alg",
    "endpoint_independent_filtering": "/axapi/v3/cgnv6/lsn/endpoint-independent-filtering",
    "endpoint_independent_mapping": "/axapi/v3/cgnv6/lsn/endpoint-independent-mapping",
    "global": "/axapi/v3/cgnv6/lsn/global",
    "health_check_gateway_list": "/axapi/v3/cgnv6/lsn/health-check-gateway/{ipv4-addr}+{ipv6-addr}",
    "inside": "/axapi/v3/cgnv6/lsn/inside",
    "performance": "/axapi/v3/cgnv6/lsn/performance",
    "port_overloading": "/axapi/v3/cgnv6/lsn/port-overloading",
    "port_reservation_list": "/axapi/v3/cgnv6/lsn/port-reservation/{inside}+{inside-port-start}+{inside-port-end}+{nat}+{nat-port-start}+{nat-port-end}",
    "radius": "/axapi/v3/cgnv6/lsn/radius",
    "stun_timeout": "/axapi/v3/cgnv6/lsn/stun-timeout",
    "tcp": "/axapi/v3/cgnv6/lsn/tcp",
}

MODULE_NAME = "lsn"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/cgnv6/lsn"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/cgnv6/lsn"
    f_dict = {}

    return url_base.format(**f_dict)