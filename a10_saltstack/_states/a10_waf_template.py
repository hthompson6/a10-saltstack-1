#!/usr/bin/python

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

try:
    from a10_saltstack import errors as a10_ex
    from a10_salstack.axapi_http import client_factory
    from a10_saltstack.kwbl import KW_IN, KW_OUT, translate_blacklist as translateBlacklist

except (ImportError) as ex:
    module.fail_json(msg="Import Error:{0}".format(ex))
except (Exception) as ex:
    module.fail_json(msg="General Exception in Ansible module import:{0}".format(ex))

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")


# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = ["allowed_http_methods","bot_check","bot_check_policy_file","brute_force_challenge_limit","brute_force_check","brute_force_global","brute_force_lockout_limit","brute_force_lockout_period","brute_force_resp_codes","brute_force_resp_codes_file","brute_force_resp_headers","brute_force_resp_headers_file","brute_force_resp_string","brute_force_resp_string_file","brute_force_test_period","ccn_mask","challenge_action_captcha","challenge_action_cookie","challenge_action_javascript","cookie_encryption_secret","cookie_name","csrf_check","decode_entities","decode_escaped_chars","decode_hex_chars","deny_non_masked_passwords","deny_non_ssl_passwords","deny_password_autocomplete","deploy_mode","disable","filter_resp_hdrs","form_consistency_check","form_deny_non_post","form_deny_non_ssl","form_set_no_cache","hide_resp_codes","hide_resp_codes_file","http_check","http_redirect","http_resp_200","http_resp_403","json_format_check","keep_end","keep_start","lifetime","log_succ_reqs","logging","mask","max_array_value_count","max_attr","max_attr_name_len","max_attr_value_len","max_cdata_len","max_cookie_len","max_cookie_name_len","max_cookie_value_len","max_cookies","max_cookies_len","max_data_parse","max_depth","max_elem","max_elem_child","max_elem_depth","max_elem_name_len","max_entities","max_entity_exp","max_entity_exp_depth","max_hdr_name_len","max_hdr_value_len","max_hdrs","max_hdrs_len","max_line_len","max_namespace","max_namespace_uri_len","max_object_member_count","max_parameter_name_len","max_parameter_total_len","max_parameter_value_len","max_parameters","max_post_size","max_query_len","max_string","max_url_len","name","pcre_mask","redirect_wlist","referer_check","referer_domain_list","referer_domain_list_only","referer_safe_url","remove_comments","remove_selfref","remove_spaces","reset_conn","resp_url_200","resp_url_403","secret_encrypted","session_check","soap_format_check","sqlia_check","sqlia_check_policy_file","ssn_mask","uri_blist_check","uri_wlist_check","url_check","user_tag","uuid","waf_blist_file","waf_wlist_file","wsdl_file","wsdl_resp_val_file","xml_format_check","xml_schema_file","xml_schema_resp_val_file","xml_sqlia_check","xml_xss_check","xss_check","xss_check_policy_file",]

__opts__ = salt.config.minion_config('/etc/salt/minion')
__grains__ = salt.laoder.grain(__opts__)


ret = dict(
    name="a10_waf_template",
    changed=False,
    original_message="",
    result={},
    comment=""
)


def get_client(**kwargs):
    run_errors = []

    a10_host = __grains__["a10_host"]
    a10_username = __grains__["a10_username"]
    a10_password =__grains__["a10_password"]
    a10_port = __grains__['port'] 
    a10_protocol = __grains__['protocol']
    version = __grains__['version']

    valid = True

    valid, validation_errors = validate(kwargs)
    map(run_errors.append, validation_errors)

    if not valid:
        err_msg = "Validation failure\n".join(run_errors)
        ret['commment'] = err_msg
        return ret 

    client = client_factory(a10_host, a10_port, a10_protocol, a10_username, a10_password)


def new_url():
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
    f_dict["name"] = kwargs["name"]

    return url_base.format(**f_dict)


def build_envelope(title, data):
    return {
        title: data
    }

def _to_axapi(key):
    return translateBlacklist(key, KW_OUT).replace("_", "-")

def _build_dict_from_param(param):
    rv = {}

    for k,v in param.items():
        hk = _to_axapi(k)
        if isinstance(v, dict):
            v_dict = _build_dict_from_param(v)
            rv[hk] = v_dict
        if isinstance(v, list):
            nv = [_build_dict_from_param(x) for x in v]
            rv[hk] = nv
        else:
            rv[hk] = v

    return rv

def build_json(title, **kwargs):
    rv = {}

    for x in AVAILABLE_PROPERTIES:
        v = module.params.get(x)
        if v:
            rx = _to_axapi(x)

            if isinstance(v, dict):
                nv = _build_dict_from_param(v)
                rv[rx] = nv
            if isinstance(v, list):
                nv = [_build_dict_from_param(x) for x in v]
                rv[rx] = nv
            else:
                rv[rx] = module.params[x]

    return build_envelope(title, rv)

def validate(**kwargs):
    # Ensure that params contains all the keys.
    requires_one_of = sorted([])
    present_keys = sorted([x for x in requires_one_of if params.get(x)])
    
    errors = []
    marg = []
    
    if not len(requires_one_of):
        return REQUIRED_VALID

    if len(present_keys) == 0:
        rc,msg = REQUIRED_NOT_SET
        marg = requires_one_of
    elif requires_one_of == present_keys:
        rc,msg = REQUIRED_MUTEX
        marg = present_keys
    else:
        rc,msg = REQUIRED_VALID
    
    if not rc:
        errors.append(msg.format(", ".join(marg)))
    
    return rc,errors

def create(**kwargs):
    payload = build_json("template", kwargs)
    try:
        client = self._get_client(**kwargs)
        post_result = client.post(new_url(kwargs), payload)
        ret["result"].update(**post_result)
        ret["changed"] = True
    except a10_ex.Exists:
        ret["changed"] = False
    except a10_ex.ACOSException as ex:
        ret["comment"] = ex.msg
        return ret
    except Exception as gex:
        raise gex
    return ret

def delete(**kwargs):
    try:
        client = self._get_client(kwargs)
        client.delete(existing_url(kwargs))
        ret["changed"] = True
    except a10_ex.NotFound:
        ret["changed"] = False
    except a10_ex.ACOSException as ex:
        ret["comment"] = ex.msg
        return ret
    except Exception as gex:
        raise gex
    return ret

def update(**kwargs):
    payload = build_json("template", kwargs)
    try:
        client = self._get_client(kwargs)
        post_result = client.put(existing_url(kwargs), payload)
        ret["result"].update(**post_result)
        ret["changed"] = True
    except a10_ex.ACOSException as ex:
        ret["comment"] = ex.msg
        return ret
    except Exception as gex:
        raise gex
    return ret