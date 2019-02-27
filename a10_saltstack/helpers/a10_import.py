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
AVAILABLE_PROPERTIES = [    "aflex",
    "auth_portal",
    "auth_portal_image",
    "auth_saml_idp",
    "bw_list",
    "ca_cert",
    "certificate_type",
    "class_list",
    "class_list_convert",
    "class_list_type",
    "dnssec_dnskey",
    "dnssec_ds",
    "file_inspection_bw_list",
    "file_inspection_use_mgmt_port",
    "geo_location",
    "glm_cert",
    "glm_license",
    "health_external",
    "health_postfile",
    "local_uri_file",
    "lw_4o6",
    "overwrite",
    "password",
    "pfx_password",
    "policy",
    "remote_file",
    "ssl_cert",
    "ssl_cert_key",
    "ssl_crl",
    "ssl_key",
    "store",
    "store_name",
    "terminal",
    "thales_kmdata",
    "thales_secworld",
    "to_device",
    "usb_license",
    "use_mgmt_port",
    "user_tag",
    "web_category_license",
    "wsdl",
    "xml_schema",
]

MODULE_NAME = "import"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/import"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/import"
    f_dict = {}

    return url_base.format(**f_dict)