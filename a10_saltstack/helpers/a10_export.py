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
AVAILABLE_PROPERTIES = ["aflex","auth_portal","auth_portal_image","axdebug","bw_list","ca_cert","class_list","csr","debug_monitor","dnssec_dnskey","dnssec_ds","externalfilename","fixed_nat","fixed_nat_archive","geo_location","local_uri_file","lw_4o6","lw_4o6_binding_table_validation_log","merged_pcap","per_cpu","policy","profile","remote_file","running_config","saml_idp_name","ssl_cert","ssl_cert_key","ssl_crl","ssl_key","startup_config","status_check","store","store_name","syslog","tgz","thales_kmdata","thales_secworld","use_mgmt_port","wsdl","xml_schema",]

MODULE_NAME = 'export'

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/export"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/export"
    f_dict = {}

    return url_base.format(**f_dict)