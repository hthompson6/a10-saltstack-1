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
AVAILABLE_PROPERTIES = ["aflex_list","auth_portal_list","bw_list_list","ca_cert_list","class_list_convert_list","class_list_list","dnssec_dnskey_list","dnssec_ds_list","file_inspection_bw_list","geo_location_list","glm_license_list","local_uri_file_list","policy_list","ssl_cert_key_list","ssl_cert_list","ssl_crl_list","ssl_key_list","thales_kmdata_list","thales_secworld_list","wsdl_list","xml_schema_list",]

REF_PROPERTIES = {
    "aflex_list": "/axapi/v3/import-periodic/aflex/{aflex}",
    "auth_portal_list": "/axapi/v3/import-periodic/auth-portal/{auth-portal}",
    "bw_list_list": "/axapi/v3/import-periodic/bw-list/{bw-list}",
    "ca_cert_list": "/axapi/v3/import-periodic/ca-cert/{ca-cert}",
    "class_list_convert_list": "/axapi/v3/import-periodic/class-list-convert/{class-list-convert}",
    "class_list_list": "/axapi/v3/import-periodic/class-list/{class-list}",
    "dnssec_dnskey_list": "/axapi/v3/import-periodic/dnssec-dnskey/{dnssec-dnskey}",
    "dnssec_ds_list": "/axapi/v3/import-periodic/dnssec-ds/{dnssec-ds}",
    "file_inspection_bw_list": "/axapi/v3/import-periodic/file-inspection-bw-list",
    "geo_location_list": "/axapi/v3/import-periodic/geo-location/{geo-location}",
    "glm_license_list": "/axapi/v3/import-periodic/glm-license/{glm-license}",
    "local_uri_file_list": "/axapi/v3/import-periodic/local-uri-file/{local-uri-file}",
    "policy_list": "/axapi/v3/import-periodic/policy/{policy}",
    "ssl_cert_key_list": "/axapi/v3/import-periodic/ssl-cert-key/{ssl-cert-key}",
    "ssl_cert_list": "/axapi/v3/import-periodic/ssl-cert/{ssl-cert}",
    "ssl_crl_list": "/axapi/v3/import-periodic/ssl-crl/{ssl-crl}",
    "ssl_key_list": "/axapi/v3/import-periodic/ssl-key/{ssl-key}",
    "thales_kmdata_list": "/axapi/v3/import-periodic/thales-kmdata/{thales-kmdata}",
    "thales_secworld_list": "/axapi/v3/import-periodic/thales-secworld/{thales-secworld}",
    "wsdl_list": "/axapi/v3/import-periodic/wsdl/{wsdl}",
    "xml_schema_list": "/axapi/v3/import-periodic/xml-schema/{xml-schema}",
}

MODULE_NAME = "import-periodic"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/import-periodic"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/import-periodic"
    f_dict = {}

    return url_base.format(**f_dict)