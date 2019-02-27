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
AVAILABLE_PROPERTIES = [    "allowed_http_methods",
    "bot_check",
    "bot_check_policy_file",
    "brute_force_challenge_limit",
    "brute_force_check",
    "brute_force_global",
    "brute_force_lockout_limit",
    "brute_force_lockout_period",
    "brute_force_resp_codes",
    "brute_force_resp_codes_file",
    "brute_force_resp_headers",
    "brute_force_resp_headers_file",
    "brute_force_resp_string",
    "brute_force_resp_string_file",
    "brute_force_test_period",
    "ccn_mask",
    "challenge_action_captcha",
    "challenge_action_cookie",
    "challenge_action_javascript",
    "cookie_encryption_secret",
    "cookie_name",
    "csrf_check",
    "decode_entities",
    "decode_escaped_chars",
    "decode_hex_chars",
    "deny_non_masked_passwords",
    "deny_non_ssl_passwords",
    "deny_password_autocomplete",
    "deploy_mode",
    "disable",
    "filter_resp_hdrs",
    "form_consistency_check",
    "form_deny_non_post",
    "form_deny_non_ssl",
    "form_set_no_cache",
    "hide_resp_codes",
    "hide_resp_codes_file",
    "http_check",
    "http_redirect",
    "http_resp_200",
    "http_resp_403",
    "json_format_check",
    "keep_end",
    "keep_start",
    "lifetime",
    "log_succ_reqs",
    "logging",
    "mask",
    "max_array_value_count",
    "max_attr",
    "max_attr_name_len",
    "max_attr_value_len",
    "max_cdata_len",
    "max_cookie_len",
    "max_cookie_name_len",
    "max_cookie_value_len",
    "max_cookies",
    "max_cookies_len",
    "max_data_parse",
    "max_depth",
    "max_elem",
    "max_elem_child",
    "max_elem_depth",
    "max_elem_name_len",
    "max_entities",
    "max_entity_exp",
    "max_entity_exp_depth",
    "max_hdr_name_len",
    "max_hdr_value_len",
    "max_hdrs",
    "max_hdrs_len",
    "max_line_len",
    "max_namespace",
    "max_namespace_uri_len",
    "max_object_member_count",
    "max_parameter_name_len",
    "max_parameter_total_len",
    "max_parameter_value_len",
    "max_parameters",
    "max_post_size",
    "max_query_len",
    "max_string",
    "max_url_len",
    "a10_name",
    "pcre_mask",
    "redirect_wlist",
    "referer_check",
    "referer_domain_list",
    "referer_domain_list_only",
    "referer_safe_url",
    "remove_comments",
    "remove_selfref",
    "remove_spaces",
    "reset_conn",
    "resp_url_200",
    "resp_url_403",
    "secret_encrypted",
    "session_check",
    "soap_format_check",
    "sqlia_check",
    "sqlia_check_policy_file",
    "ssn_mask",
    "uri_blist_check",
    "uri_wlist_check",
    "url_check",
    "user_tag",
    "uuid",
    "waf_blist_file",
    "waf_wlist_file",
    "wsdl_file",
    "wsdl_resp_val_file",
    "xml_format_check",
    "xml_schema_file",
    "xml_schema_resp_val_file",
    "xml_sqlia_check",
    "xml_xss_check",
    "xss_check",
    "xss_check_policy_file",
]

MODULE_NAME = "template"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/waf/template/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/waf/template/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["a10-name"]

    return url_base.format(**f_dict)