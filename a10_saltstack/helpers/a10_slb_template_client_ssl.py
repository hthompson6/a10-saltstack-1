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
    "auth_sg",
    "auth_sg_dn",
    "auth_sg_filter",
    "auth_username",
    "auth_username_attribute",
    "authen_name",
    "authorization",
    "ca_certs",
    "cache_persistence_list_name",
    "case_insensitive",
    "cert",
    "cert_revoke_action",
    "cert_unknown_action",
    "chain_cert",
    "cipher_without_prio_list",
    "class_list_name",
    "client_auth_case_insensitive",
    "client_auth_class_list",
    "client_auth_contains_list",
    "client_auth_ends_with_list",
    "client_auth_equals_list",
    "client_auth_starts_with_list",
    "client_certificate",
    "close_notify",
    "contains_list",
    "crl_certs",
    "dgversion",
    "dh_type",
    "disable_sslv3",
    "ec_list",
    "enable_tls_alert_logging",
    "ends_with_list",
    "equals_list",
    "exception_class_list",
    "expire_hours",
    "forward_encrypted",
    "forward_passphrase",
    "forward_proxy_alt_sign",
    "forward_proxy_ca_cert",
    "forward_proxy_ca_key",
    "forward_proxy_cert_cache_limit",
    "forward_proxy_cert_cache_timeout",
    "forward_proxy_cert_expiry",
    "forward_proxy_cert_not_ready_action",
    "forward_proxy_cert_revoke_action",
    "forward_proxy_cert_unknown_action",
    "forward_proxy_crl_disable",
    "forward_proxy_decrypted_dscp",
    "forward_proxy_decrypted_dscp_bypass",
    "forward_proxy_enable",
    "forward_proxy_failsafe_disable",
    "forward_proxy_log_disable",
    "forward_proxy_ocsp_disable",
    "forward_proxy_selfsign_redir",
    "forward_proxy_ssl_version",
    "forward_proxy_trusted_ca_lists",
    "forward_proxy_verify_cert_fail_action",
    "fp_alt_cert",
    "fp_alt_encrypted",
    "fp_alt_key",
    "fp_alt_passphrase",
    "fp_cert_ext_aia_ca_issuers",
    "fp_cert_ext_aia_ocsp",
    "fp_cert_ext_crldp",
    "fp_cert_fetch_autonat",
    "fp_cert_fetch_autonat_precedence",
    "fp_cert_fetch_natpool_name",
    "fp_cert_fetch_natpool_precedence",
    "handshake_logging_enable",
    "hsm_type",
    "inspect_list_name",
    "key",
    "key_encrypted",
    "key_passphrase",
    "ldap_base_dn_from_cert",
    "ldap_search_filter",
    "local_logging",
    "multi_class_list",
    "a10_name",
    "non_ssl_bypass_service_group",
    "notafter",
    "notafterday",
    "notaftermonth",
    "notafteryear",
    "notbefore",
    "notbeforeday",
    "notbeforemonth",
    "notbeforeyear",
    "ocsp_stapling",
    "ocspst_ca_cert",
    "ocspst_ocsp",
    "ocspst_sg",
    "ocspst_sg_days",
    "ocspst_sg_hours",
    "ocspst_sg_minutes",
    "ocspst_sg_timeout",
    "ocspst_srvr",
    "ocspst_srvr_days",
    "ocspst_srvr_hours",
    "ocspst_srvr_minutes",
    "ocspst_srvr_timeout",
    "renegotiation_disable",
    "req_ca_lists",
    "server_name_auto_map",
    "server_name_list",
    "session_cache_size",
    "session_cache_timeout",
    "session_ticket_lifetime",
    "sni_enable_log",
    "ssl_false_start_disable",
    "ssli_logging",
    "sslilogging",
    "sslv2_bypass_service_group",
    "starts_with_list",
    "template_cipher",
    "template_hsm",
    "user_tag",
    "uuid",
    "verify_cert_fail_action",
    "version",
    "web_category",
]

REF_PROPERTIES = [
    "auth_sg",
    "authen_name",
    "exception_class_list",
    "fp_cert_fetch_natpool_name",
    "non_ssl_bypass_service_group",
    "ocspst_sg",
    "ocspst_srvr",
    "sslv2_bypass_service_group",
    "template_cipher",
]

MODULE_NAME = "client-ssl"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/template/client-ssl/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/template/client-ssl/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["a10-name"]

    return url_base.format(**f_dict)