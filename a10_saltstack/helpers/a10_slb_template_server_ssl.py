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
AVAILABLE_PROPERTIES = [
    "alert_type",
    "ca_certs",
    "cert",
    "cipher_template",
    "cipher_without_prio_list",
    "close_notify",
    "crl_certs",
    "dgversion",
    "dh_type",
    "ec_list",
    "enable_tls_alert_logging",
    "encrypted",
    "forward_proxy_enable",
    "handshake_logging_enable",
    "key",
    "a10_name",
    "ocsp_stapling",
    "passphrase",
    "renegotiation_disable",
    "server_certificate_error",
    "session_cache_size",
    "session_cache_timeout",
    "session_ticket_enable",
    "ssli_logging",
    "sslilogging",
    "use_client_sni",
    "user_tag",
    "uuid",
    "version",
]

REF_PROPERTIES = [
    "cipher-template",
]

MODULE_NAME = "server-ssl"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/template/server-ssl/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/template/server-ssl/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["a10-name"]

    return url_base.format(**f_dict)