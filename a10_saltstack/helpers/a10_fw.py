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
AVAILABLE_PROPERTIES = ["active_rule_set","alg","app","apply_changes","clear_session_filter","global","gtp","helper_sessions","local_log","logging","radius","server_list","service_group_list","session_aging_list","tcp","tcp_rst_close_immediate","tcp_window_check","template","urpf","vrid",]

REF_PROPERTIES = {
    "active_rule_set": "/axapi/v3/fw/active-rule-set",
    "alg": "/axapi/v3/fw/alg",
    "app": "/axapi/v3/fw/app",
    "apply_changes": "/axapi/v3/fw/apply-changes",
    "clear_session_filter": "/axapi/v3/fw/clear-session-filter",
    "global": "/axapi/v3/fw/global",
    "gtp": "/axapi/v3/fw/gtp",
    "helper_sessions": "/axapi/v3/fw/helper-sessions",
    "local_log": "/axapi/v3/fw/local-log",
    "logging": "/axapi/v3/fw/logging",
    "radius": "/axapi/v3/fw/radius",
    "server_list": "/axapi/v3/fw/server/{name}",
    "service_group_list": "/axapi/v3/fw/service-group/{name}",
    "session_aging_list": "/axapi/v3/fw/session-aging/{name}",
    "tcp": "/axapi/v3/fw/tcp",
    "tcp_rst_close_immediate": "/axapi/v3/fw/tcp-rst-close-immediate",
    "tcp_window_check": "/axapi/v3/fw/tcp-window-check",
    "template": "/axapi/v3/fw/template",
    "urpf": "/axapi/v3/fw/urpf",
    "vrid": "/axapi/v3/fw/vrid",
}

MODULE_NAME = "fw"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/fw"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/fw"
    f_dict = {}

    return url_base.format(**f_dict)