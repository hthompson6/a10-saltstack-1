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
AVAILABLE_PROPERTIES = ["auditlog","buffered","console","disable_partition_name","email","email_address","export","facility","host","local_log","lsn","monitor","single_priority_list","syslog","trap",]

REF_PROPERTIES = {
    "auditlog": "/axapi/v3/logging/auditlog",
    "buffered": "/axapi/v3/logging/buffered",
    "console": "/axapi/v3/logging/console",
    "disable_partition_name": "/axapi/v3/logging/disable-partition-name",
    "email": "/axapi/v3/logging/email",
    "email_address": "/axapi/v3/logging/email-address",
    "export": "/axapi/v3/logging/export",
    "facility": "/axapi/v3/logging/facility",
    "host": "/axapi/v3/logging/host",
    "local_log": "/axapi/v3/logging/local-log",
    "lsn": "/axapi/v3/logging/lsn",
    "monitor": "/axapi/v3/logging/monitor",
    "single_priority_list": "/axapi/v3/logging/single-priority/{levelname}",
    "syslog": "/axapi/v3/logging/syslog",
    "trap": "/axapi/v3/logging/trap",
}

MODULE_NAME = "logging"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/logging"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/logging"
    f_dict = {}

    return url_base.format(**f_dict)