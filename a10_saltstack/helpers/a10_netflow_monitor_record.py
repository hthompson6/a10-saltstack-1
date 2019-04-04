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
    "dslite",
    "nat44",
    "nat64",
    "netflow_v5",
    "netflow_v5_ext",
    "port_batch_dslite",
    "port_batch_nat44",
    "port_batch_nat64",
    "port_batch_v2_dslite",
    "port_batch_v2_nat44",
    "port_batch_v2_nat64",
    "port_mapping_dslite",
    "port_mapping_nat44",
    "port_mapping_nat64",
    "sesn_event_dslite",
    "sesn_event_fw4",
    "sesn_event_fw6",
    "sesn_event_nat44",
    "sesn_event_nat64",
    "uuid",
    "monitor_name",
]

REF_PROPERTIES = [
]

MODULE_NAME = "record"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/netflow/monitor/{monitor_name}/record"
    f_dict = {}
    f_dict["monitor_name"] = kwargs["monitor_name"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/netflow/monitor/{monitor_name}/record"
    f_dict = {}
    f_dict["monitor_name"] = kwargs["monitor_name"]

    return url_base.format(**f_dict)