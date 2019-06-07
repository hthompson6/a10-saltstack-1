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
AVAILABLE_PROPERTIES = ["compound","database","dns","external","ftp","http","https","icmp","imap","kerberos_kdc","ldap","ntp","pop3","radius","rtsp","sip","smtp","snmp","tacplus","tcp","udp","monitor_name",]

REF_PROPERTIES = {
    "compound": "/axapi/v3/health/monitor/{name}/method/compound",
    "database": "/axapi/v3/health/monitor/{name}/method/database",
    "dns": "/axapi/v3/health/monitor/{name}/method/dns",
    "external": "/axapi/v3/health/monitor/{name}/method/external",
    "ftp": "/axapi/v3/health/monitor/{name}/method/ftp",
    "http": "/axapi/v3/health/monitor/{name}/method/http",
    "https": "/axapi/v3/health/monitor/{name}/method/https",
    "icmp": "/axapi/v3/health/monitor/{name}/method/icmp",
    "imap": "/axapi/v3/health/monitor/{name}/method/imap",
    "kerberos_kdc": "/axapi/v3/health/monitor/{name}/method/kerberos-kdc",
    "ldap": "/axapi/v3/health/monitor/{name}/method/ldap",
    "ntp": "/axapi/v3/health/monitor/{name}/method/ntp",
    "pop3": "/axapi/v3/health/monitor/{name}/method/pop3",
    "radius": "/axapi/v3/health/monitor/{name}/method/radius",
    "rtsp": "/axapi/v3/health/monitor/{name}/method/rtsp",
    "sip": "/axapi/v3/health/monitor/{name}/method/sip",
    "smtp": "/axapi/v3/health/monitor/{name}/method/smtp",
    "snmp": "/axapi/v3/health/monitor/{name}/method/snmp",
    "tacplus": "/axapi/v3/health/monitor/{name}/method/tacplus",
    "tcp": "/axapi/v3/health/monitor/{name}/method/tcp",
    "udp": "/axapi/v3/health/monitor/{name}/method/udp",
}

MODULE_NAME = "method"

PARENT_KEYS = ["monitor_name",]

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/health/monitor/{monitor_name}/method"
    f_dict = {}
    f_dict["monitor_name"] = kwargs["monitor_name"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/health/monitor/{monitor_name}/method"
    f_dict = {}
    f_dict["monitor_name"] = kwargs["monitor_name"]

    return url_base.format(**f_dict)