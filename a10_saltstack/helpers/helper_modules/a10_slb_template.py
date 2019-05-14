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
AVAILABLE_PROPERTIES = ["cache_list","cipher_list","client_ssl_list","connection_reuse_list","dblb_list","diameter_list","dns_list","dynamic_service_list","external_service_list","fix_list","ftp_list","http_list","http_policy_list","imap_pop3_list","logging_list","monitor_list","persist","policy_list","port_list","reqmod_icap_list","respmod_icap_list","server_list","server_ssl_list","sip_list","smpp_list","smtp_list","ssli_list","tcp_list","tcp_proxy_list","udp_list","virtual_port_list","virtual_server_list",]

REF_PROPERTIES = {
    "cache_list": "/axapi/v3/slb/template/cache/{name}",
    "cipher_list": "/axapi/v3/slb/template/cipher/{name}",
    "client_ssl_list": "/axapi/v3/slb/template/client-ssl/{name}",
    "connection_reuse_list": "/axapi/v3/slb/template/connection-reuse/{name}",
    "dblb_list": "/axapi/v3/slb/template/dblb/{name}",
    "diameter_list": "/axapi/v3/slb/template/diameter/{name}",
    "dns_list": "/axapi/v3/slb/template/dns/{name}",
    "dynamic_service_list": "/axapi/v3/slb/template/dynamic-service/{name}",
    "external_service_list": "/axapi/v3/slb/template/external-service/{name}",
    "fix_list": "/axapi/v3/slb/template/fix/{name}",
    "ftp_list": "/axapi/v3/slb/template/ftp/{name}",
    "http_list": "/axapi/v3/slb/template/http/{name}",
    "http_policy_list": "/axapi/v3/slb/template/http-policy/{name}",
    "imap_pop3_list": "/axapi/v3/slb/template/imap-pop3/{name}",
    "logging_list": "/axapi/v3/slb/template/logging/{name}",
    "monitor_list": "/axapi/v3/slb/template/monitor/{id}",
    "persist": "/axapi/v3/slb/template/persist",
    "policy_list": "/axapi/v3/slb/template/policy/{name}",
    "port_list": "/axapi/v3/slb/template/port/{name}",
    "reqmod_icap_list": "/axapi/v3/slb/template/reqmod-icap/{name}",
    "respmod_icap_list": "/axapi/v3/slb/template/respmod-icap/{name}",
    "server_list": "/axapi/v3/slb/template/server/{name}",
    "server_ssl_list": "/axapi/v3/slb/template/server-ssl/{name}",
    "sip_list": "/axapi/v3/slb/template/sip/{name}",
    "smpp_list": "/axapi/v3/slb/template/smpp/{name}",
    "smtp_list": "/axapi/v3/slb/template/smtp/{name}",
    "ssli_list": "/axapi/v3/slb/template/ssli/{name}",
    "tcp_list": "/axapi/v3/slb/template/tcp/{name}",
    "tcp_proxy_list": "/axapi/v3/slb/template/tcp-proxy/{name}",
    "udp_list": "/axapi/v3/slb/template/udp/{name}",
    "virtual_port_list": "/axapi/v3/slb/template/virtual-port/{name}",
    "virtual_server_list": "/axapi/v3/slb/template/virtual-server/{name}",
}

MODULE_NAME = "template"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/template"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/template"
    f_dict = {}

    return url_base.format(**f_dict)