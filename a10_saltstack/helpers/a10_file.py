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
AVAILABLE_PROPERTIES = ["aflex","auth_portal","auth_portal_image","auth_saml_idp","axdebug","bw_list","ca_cert","class_list","csr","debug_monitor","dnssec_dnskey","dnssec_ds","file_inspection_bw_list","glm_cert","glm_license","health_external","health_postfile","license","local_uri_file","log_backup","policy","ssh_pubkey","ssl_cert","ssl_cert_key","ssl_crl","ssl_key","startup_config","syslog","system_backup","techsupport","template","web_category_license","web_service_cert_key","wsdl","xml_schema",]

REF_PROPERTIES = {
    "aflex": "/axapi/v3/file/aflex",
    "auth_portal": "/axapi/v3/file/auth-portal",
    "auth_portal_image": "/axapi/v3/file/auth-portal-image",
    "auth_saml_idp": "/axapi/v3/file/auth-saml-idp",
    "axdebug": "/axapi/v3/file/axdebug",
    "bw_list": "/axapi/v3/file/bw-list",
    "ca_cert": "/axapi/v3/file/ca-cert",
    "class_list": "/axapi/v3/file/class-list",
    "csr": "/axapi/v3/file/csr",
    "debug_monitor": "/axapi/v3/file/debug-monitor",
    "dnssec_dnskey": "/axapi/v3/file/dnssec-dnskey",
    "dnssec_ds": "/axapi/v3/file/dnssec-ds",
    "file_inspection_bw_list": "/axapi/v3/file/file-inspection-bw-list",
    "glm_cert": "/axapi/v3/file/glm-cert",
    "glm_license": "/axapi/v3/file/glm-license",
    "health_external": "/axapi/v3/file/health-external",
    "health_postfile": "/axapi/v3/file/health-postfile",
    "license": "/axapi/v3/file/license",
    "local_uri_file": "/axapi/v3/file/local-uri-file",
    "log_backup": "/axapi/v3/file/log-backup",
    "policy": "/axapi/v3/file/policy",
    "ssh_pubkey": "/axapi/v3/file/ssh-pubkey",
    "ssl_cert": "/axapi/v3/file/ssl-cert",
    "ssl_cert_key": "/axapi/v3/file/ssl-cert-key",
    "ssl_crl": "/axapi/v3/file/ssl-crl",
    "ssl_key": "/axapi/v3/file/ssl-key",
    "startup_config": "/axapi/v3/file/startup-config",
    "syslog": "/axapi/v3/file/syslog",
    "system_backup": "/axapi/v3/file/system-backup",
    "techsupport": "/axapi/v3/file/techsupport",
    "template": "/axapi/v3/file/template",
    "web_category_license": "/axapi/v3/file/web-category-license",
    "web_service_cert_key": "/axapi/v3/file/web-service-cert-key",
    "wsdl": "/axapi/v3/file/wsdl",
    "xml_schema": "/axapi/v3/file/xml-schema",
}

MODULE_NAME = "file"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/file"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/file"
    f_dict = {}

    return url_base.format(**f_dict)