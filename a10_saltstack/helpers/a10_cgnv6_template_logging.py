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
    "batched_logging_disable",
    "custom",
    "disable_log_by_destination",
    "facility",
    "format",
    "include_destination",
    "include_http",
    "include_inside_user_mac",
    "include_partition_name",
    "include_radius_attribute",
    "include_session_byte_count",
    "log",
    "log_receiver",
    "a10_name",
    "resolution",
    "rfc_custom",
    "rule",
    "service_group",
    "severity",
    "shared",
    "source_address",
    "source_port",
    "user_tag",
    "uuid",
]

REF_PROPERTIES = {
    "disable_log_by_destination": "/axapi/v3/cgnv6/template/logging/{name}/disable-log-by-destination",
    "source_address": "/axapi/v3/cgnv6/template/logging/{name}/source-address",
}

MODULE_NAME = "logging"

PARENT_KEYS = []

CHILD_KEYS = ["name",]


def new_url():
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/cgnv6/template/logging/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url():
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/cgnv6/template/logging/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["a10-name"]

    return url_base.format(**f_dict)