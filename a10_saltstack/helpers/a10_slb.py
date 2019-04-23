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
AVAILABLE_PROPERTIES = ["aflow","common","connection_reuse","crl_srcip","dns","dns_cache","fast_http_proxy","fix","ftp_ctl","ftp_data","ftp_proxy","generic_proxy","health_gateway","health_stat","http_proxy","http2","hw_compress","icap","icap_http","imap_proxy","l4","l7session","mssql","mysql","passthrough","perf","persist","player_id_global","player_id_list","pop3_proxy","proxy","rate_limit_log","rc_cache_global","resource_usage","server_list","service_group_list","sip","smpp","smtp","spdy_proxy","sport_rate_limit","ssl_cert_revoke","ssl_expire_check","ssl_forward_proxy","svm_source_nat","switch","telemetry_log","template","transparent_acl_template","transparent_tcp_template","virtual_server_list",]

REF_PROPERTIES = {
    "aflow": "/axapi/v3/slb/aflow",
    "common": "/axapi/v3/slb/common",
    "connection_reuse": "/axapi/v3/slb/connection-reuse",
    "crl_srcip": "/axapi/v3/slb/crl-srcip",
    "dns": "/axapi/v3/slb/dns",
    "dns_cache": "/axapi/v3/slb/dns-cache",
    "fast_http_proxy": "/axapi/v3/slb/fast-http-proxy",
    "fix": "/axapi/v3/slb/fix",
    "ftp_ctl": "/axapi/v3/slb/ftp-ctl",
    "ftp_data": "/axapi/v3/slb/ftp-data",
    "ftp_proxy": "/axapi/v3/slb/ftp-proxy",
    "generic_proxy": "/axapi/v3/slb/generic-proxy",
    "health_gateway": "/axapi/v3/slb/health-gateway",
    "health_stat": "/axapi/v3/slb/health-stat",
    "http_proxy": "/axapi/v3/slb/http-proxy",
    "http2": "/axapi/v3/slb/http2",
    "hw_compress": "/axapi/v3/slb/hw-compress",
    "icap": "/axapi/v3/slb/icap",
    "icap_http": "/axapi/v3/slb/icap_http",
    "imap_proxy": "/axapi/v3/slb/imap-proxy",
    "l4": "/axapi/v3/slb/l4",
    "l7session": "/axapi/v3/slb/l7session",
    "mssql": "/axapi/v3/slb/mssql",
    "mysql": "/axapi/v3/slb/mysql",
    "passthrough": "/axapi/v3/slb/passthrough",
    "perf": "/axapi/v3/slb/perf",
    "persist": "/axapi/v3/slb/persist",
    "player_id_global": "/axapi/v3/slb/player-id-global",
    "player_id_list": "/axapi/v3/slb/player-id-list",
    "pop3_proxy": "/axapi/v3/slb/pop3-proxy",
    "proxy": "/axapi/v3/slb/proxy",
    "rate_limit_log": "/axapi/v3/slb/rate-limit-log",
    "rc_cache_global": "/axapi/v3/slb/rc-cache-global",
    "resource_usage": "/axapi/v3/slb/resource-usage",
    "server_list": "/axapi/v3/slb/server/{name}",
    "service_group_list": "/axapi/v3/slb/service-group/{name}",
    "sip": "/axapi/v3/slb/sip",
    "smpp": "/axapi/v3/slb/smpp",
    "smtp": "/axapi/v3/slb/smtp",
    "spdy_proxy": "/axapi/v3/slb/spdy-proxy",
    "sport_rate_limit": "/axapi/v3/slb/sport-rate-limit",
    "ssl_cert_revoke": "/axapi/v3/slb/ssl-cert-revoke",
    "ssl_expire_check": "/axapi/v3/slb/ssl-expire-check",
    "ssl_forward_proxy": "/axapi/v3/slb/ssl-forward-proxy",
    "svm_source_nat": "/axapi/v3/slb/svm-source-nat",
    "switch": "/axapi/v3/slb/switch",
    "telemetry_log": "/axapi/v3/slb/telemetry-log",
    "template": "/axapi/v3/slb/template",
    "transparent_acl_template": "/axapi/v3/slb/transparent-acl-template",
    "transparent_tcp_template": "/axapi/v3/slb/transparent-tcp-template",
    "virtual_server_list": "/axapi/v3/slb/virtual-server/{name}",
}

MODULE_NAME = "slb"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb"
    f_dict = {}

    return url_base.format(**f_dict)