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
AVAILABLE_PROPERTIES = [    "all",
    "end_address",
    "exclude_ip",
    "group",
    "max_users_per_ip",
    "netmask",
    "partition",
    "per_batch_port_usage_warning_threshold",
    "pool_name",
    "port_batch_v2_size",
    "shared",
    "simultaneous_batch_allocation",
    "start_address",
    "tcp_time_wait_interval",
    "usable_nat_ports",
    "usable_nat_ports_end",
    "usable_nat_ports_start",
    "uuid",
    "vrid",
]

MODULE_NAME = "pool"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/cgnv6/nat/pool/{pool-name}"
    f_dict = {}
    f_dict["pool-name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/cgnv6/nat/pool/{pool-name}"
    f_dict = {}
    f_dict["pool-name"] = kwargs["pool_name"]

    return url_base.format(**f_dict)