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
AVAILABLE_PROPERTIES = ["inside","inside_addr","inside_end_port","inside_start_port","nat","nat_end_port","nat_start_port","tunnel_dest_address","uuid",]

MODULE_NAME = 'port-reservation'

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/cgnv6/ds-lite/port-reservation/{inside}+{tunnel-dest-address}+{inside-addr}+{inside-start-port}+{inside-end-port}+{nat}+{nat-start-port}+{nat-end-port}"
    f_dict = {}
    f_dict["inside"] = ""
    f_dict["tunnel-dest-address"] = ""
    f_dict["inside-addr"] = ""
    f_dict["inside-start-port"] = ""
    f_dict["inside-end-port"] = ""
    f_dict["nat"] = ""
    f_dict["nat-start-port"] = ""
    f_dict["nat-end-port"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/cgnv6/ds-lite/port-reservation/{inside}+{tunnel-dest-address}+{inside-addr}+{inside-start-port}+{inside-end-port}+{nat}+{nat-start-port}+{nat-end-port}"
    f_dict = {}
    f_dict["inside"] = kwargs["inside"]
    f_dict["tunnel-dest-address"] = kwargs["tunnel-dest-address"]
    f_dict["inside-addr"] = kwargs["inside-addr"]
    f_dict["inside-start-port"] = kwargs["inside-start-port"]
    f_dict["inside-end-port"] = kwargs["inside-end-port"]
    f_dict["nat"] = kwargs["nat"]
    f_dict["nat-start-port"] = kwargs["nat-start-port"]
    f_dict["nat-end-port"] = kwargs["nat-end-port"]

    return url_base.format(**f_dict)