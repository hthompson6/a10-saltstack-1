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
    "ftp",
    "icmp",
    "pptp",
    "rtsp",
    "sip",
    "tftp",
    "uuid",
]

REF_PROPERTIES = {
    "dns": "/axapi/v3/fw/alg/dns",
    "ftp": "/axapi/v3/fw/alg/ftp",
    "icmp": "/axapi/v3/fw/alg/icmp",
    "pptp": "/axapi/v3/fw/alg/pptp",
    "rtsp": "/axapi/v3/fw/alg/rtsp",
    "sip": "/axapi/v3/fw/alg/sip",
    "tftp": "/axapi/v3/fw/alg/tftp",
}

MODULE_NAME = "alg"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/fw/alg"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/fw/alg"
    f_dict = {}

    return url_base.format(**f_dict)