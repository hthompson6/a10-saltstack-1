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
AVAILABLE_PROPERTIES = ["common","fail_over_policy_template_list","force_self_standby","force_self_standby_persistent_list","interface","l2_inline_peer_ip_list","l3_inline_mode_flag","ospf_inline_list","peer_group","preferred_session_sync_port","restart_port_list","state","vrid_lead_list","vrid_list",]

REF_PROPERTIES = {
    "common": "/axapi/v3/vrrp-a/common",
    "fail_over_policy_template_list": "/axapi/v3/vrrp-a/fail-over-policy-template/{name}",
    "force_self_standby": "/axapi/v3/vrrp-a/force-self-standby",
    "force_self_standby_persistent_list": "/axapi/v3/vrrp-a/force-self-standby-persistent/{vrid}",
    "interface": "/axapi/v3/vrrp-a/interface",
    "l2_inline_peer_ip_list": "/axapi/v3/vrrp-a/l2-inline-peer-ip/{ip-address}",
    "l3_inline_mode_flag": "/axapi/v3/vrrp-a/l3-inline-mode-flag",
    "ospf_inline_list": "/axapi/v3/vrrp-a/ospf-inline/{vlan}",
    "peer_group": "/axapi/v3/vrrp-a/peer-group",
    "preferred_session_sync_port": "/axapi/v3/vrrp-a/preferred-session-sync-port",
    "restart_port_list": "/axapi/v3/vrrp-a/restart-port-list",
    "state": "/axapi/v3/vrrp-a/state",
    "vrid_lead_list": "/axapi/v3/vrrp-a/vrid-lead/{vrid-lead-str}",
    "vrid_list": "/axapi/v3/vrrp-a/vrid/{vrid-val}",
}

MODULE_NAME = "vrrp-a"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/vrrp-a"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/vrrp-a"
    f_dict = {}

    return url_base.format(**f_dict)