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
AVAILABLE_PROPERTIES = ["esp","ftp","h323","mgcp","pptp","rtsp","sip","tftp",]

REF_PROPERTIES = {
    "esp": "/axapi/v3/cgnv6/nat64/alg/esp",
    "ftp": "/axapi/v3/cgnv6/nat64/alg/ftp",
    "h323": "/axapi/v3/cgnv6/nat64/alg/h323",
    "mgcp": "/axapi/v3/cgnv6/nat64/alg/mgcp",
    "pptp": "/axapi/v3/cgnv6/nat64/alg/pptp",
    "rtsp": "/axapi/v3/cgnv6/nat64/alg/rtsp",
    "sip": "/axapi/v3/cgnv6/nat64/alg/sip",
    "tftp": "/axapi/v3/cgnv6/nat64/alg/tftp",
}

MODULE_NAME = "alg"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/cgnv6/nat64/alg"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/cgnv6/nat64/alg"
    f_dict = {}

    return url_base.format(**f_dict)