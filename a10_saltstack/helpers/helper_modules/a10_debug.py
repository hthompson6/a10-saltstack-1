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
AVAILABLE_PROPERTIES = ["a10support","aflex","aflow","all","appcls","auth","backtrace","bgp","bridge_vlan_group","cache_list","cli","cpu","diameter","dumpthread","es","fix","ftp","ftp_proxy","fw","generic_proxy","h323","ha","hm_list","http_proxy","http2","hw_compression_list","imap_proxy","imish","imish_profile","ip","ipv6","isis","l4","l7session","lacp","layer2","lb","list_all_cli","local_log","logging","lsn","management","mgcp","migration_list","mlb","monitor","msg_proxy","ospf","packet","polltech_enable","pop3_proxy","rip","rt","scaleout","sctp","sess","sip","smpp","snmp","ssl","ssli","system","tcp","threat_intel","tunnel","vector","vpn","vtep_error","vtep_event","vtep_packet","waf","web_category",]

REF_PROPERTIES = {
    "a10support": "/axapi/v3/debug/a10support",
    "aflex": "/axapi/v3/debug/aflex",
    "aflow": "/axapi/v3/debug/aflow",
    "all": "/axapi/v3/debug/all",
    "appcls": "/axapi/v3/debug/appcls",
    "auth": "/axapi/v3/debug/auth",
    "backtrace": "/axapi/v3/debug/backtrace",
    "bgp": "/axapi/v3/debug/bgp",
    "bridge_vlan_group": "/axapi/v3/debug/bridge-vlan-group",
    "cache_list": "/axapi/v3/debug/cache/{level}",
    "cli": "/axapi/v3/debug/cli",
    "cpu": "/axapi/v3/debug/cpu",
    "diameter": "/axapi/v3/debug/diameter",
    "dumpthread": "/axapi/v3/debug/dumpthread",
    "es": "/axapi/v3/debug/es",
    "fix": "/axapi/v3/debug/fix",
    "ftp": "/axapi/v3/debug/ftp",
    "ftp_proxy": "/axapi/v3/debug/ftp-proxy",
    "fw": "/axapi/v3/debug/fw",
    "generic_proxy": "/axapi/v3/debug/generic-proxy",
    "h323": "/axapi/v3/debug/h323",
    "ha": "/axapi/v3/debug/ha",
    "hm_list": "/axapi/v3/debug/hm/{level}",
    "http_proxy": "/axapi/v3/debug/http-proxy",
    "http2": "/axapi/v3/debug/http2",
    "hw_compression_list": "/axapi/v3/debug/hw-compression/{level}",
    "imap_proxy": "/axapi/v3/debug/imap-proxy",
    "imish": "/axapi/v3/debug/imish",
    "imish_profile": "/axapi/v3/debug/imish-profile",
    "ip": "/axapi/v3/debug/ip",
    "ipv6": "/axapi/v3/debug/ipv6",
    "isis": "/axapi/v3/debug/isis",
    "l4": "/axapi/v3/debug/l4",
    "l7session": "/axapi/v3/debug/l7session",
    "lacp": "/axapi/v3/debug/lacp",
    "layer2": "/axapi/v3/debug/layer2",
    "lb": "/axapi/v3/debug/lb",
    "list_all_cli": "/axapi/v3/debug/list_all_cli",
    "local_log": "/axapi/v3/debug/local-log",
    "logging": "/axapi/v3/debug/logging",
    "lsn": "/axapi/v3/debug/lsn",
    "management": "/axapi/v3/debug/management",
    "mgcp": "/axapi/v3/debug/mgcp",
    "migration_list": "/axapi/v3/debug/migration/{dumy}",
    "mlb": "/axapi/v3/debug/mlb",
    "monitor": "/axapi/v3/debug/monitor",
    "msg_proxy": "/axapi/v3/debug/msg-proxy",
    "ospf": "/axapi/v3/debug/ospf",
    "packet": "/axapi/v3/debug/packet",
    "polltech_enable": "/axapi/v3/debug/polltech-enable",
    "pop3_proxy": "/axapi/v3/debug/pop3-proxy",
    "rip": "/axapi/v3/debug/rip",
    "rt": "/axapi/v3/debug/rt",
    "scaleout": "/axapi/v3/debug/scaleout",
    "sctp": "/axapi/v3/debug/sctp",
    "sess": "/axapi/v3/debug/sess",
    "sip": "/axapi/v3/debug/sip",
    "smpp": "/axapi/v3/debug/smpp",
    "snmp": "/axapi/v3/debug/snmp",
    "ssl": "/axapi/v3/debug/ssl",
    "ssli": "/axapi/v3/debug/ssli",
    "system": "/axapi/v3/debug/system",
    "tcp": "/axapi/v3/debug/tcp",
    "threat_intel": "/axapi/v3/debug/threat-intel",
    "tunnel": "/axapi/v3/debug/tunnel",
    "vector": "/axapi/v3/debug/vector",
    "vpn": "/axapi/v3/debug/vpn",
    "vtep_error": "/axapi/v3/debug/vtep-error",
    "vtep_event": "/axapi/v3/debug/vtep-event",
    "vtep_packet": "/axapi/v3/debug/vtep-packet",
    "waf": "/axapi/v3/debug/waf",
    "web_category": "/axapi/v3/debug/web-category",
}

MODULE_NAME = "debug"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/debug"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/debug"
    f_dict = {}

    return url_base.format(**f_dict)