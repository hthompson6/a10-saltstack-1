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
    "buffer_drop",
    "buffer_usage",
    "conn_type0",
    "conn_type1",
    "conn_type2",
    "conn_type3",
    "conn_type4",
    "ctrl_cpu",
    "data_cpu",
    "disk",
    "memory",
    "smp_type0",
    "smp_type1",
    "smp_type2",
    "smp_type3",
    "smp_type4",
    "uuid",
    "warn_temp",
]

REF_PROPERTIES = {
}

MODULE_NAME = "monitor"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url():
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/monitor"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url():
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/monitor"
    f_dict = {}

    return url_base.format(**f_dict)