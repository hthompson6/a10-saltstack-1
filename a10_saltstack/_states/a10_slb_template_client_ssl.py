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
AVAILABLE_PROPERTIES = ["alert_type","auth_sg","auth_sg_dn","auth_sg_filter","auth_username","auth_username_attribute","authen_name","authorization","ca_certs","cache_persistence_list_name","case_insensitive","cert","cert_revoke_action","cert_unknown_action","chain_cert","cipher_without_prio_list","class_list_name","client_auth_case_insensitive","client_auth_class_list","client_auth_contains_list","client_auth_ends_with_list","client_auth_equals_list","client_auth_starts_with_list","client_certificate","close_notify","contains_list","crl_certs","dgversion","dh_type","disable_sslv3","ec_list","enable_tls_alert_logging","ends_with_list","equals_list","exception_class_list","expire_hours","forward_encrypted","forward_passphrase","forward_proxy_alt_sign","forward_proxy_ca_cert","forward_proxy_ca_key","forward_proxy_cert_cache_limit","forward_proxy_cert_cache_timeout","forward_proxy_cert_expiry","forward_proxy_cert_not_ready_action","forward_proxy_cert_revoke_action","forward_proxy_cert_unknown_action","forward_proxy_crl_disable","forward_proxy_decrypted_dscp","forward_proxy_decrypted_dscp_bypass","forward_proxy_enable","forward_proxy_failsafe_disable","forward_proxy_log_disable","forward_proxy_ocsp_disable","forward_proxy_selfsign_redir","forward_proxy_ssl_version","forward_proxy_trusted_ca_lists","forward_proxy_verify_cert_fail_action","fp_alt_cert","fp_alt_encrypted","fp_alt_key","fp_alt_passphrase","fp_cert_ext_aia_ca_issuers","fp_cert_ext_aia_ocsp","fp_cert_ext_crldp","fp_cert_fetch_autonat","fp_cert_fetch_autonat_precedence","fp_cert_fetch_natpool_name","fp_cert_fetch_natpool_precedence","handshake_logging_enable","hsm_type","inspect_list_name","key","key_encrypted","key_passphrase","ldap_base_dn_from_cert","ldap_search_filter","local_logging","multi_class_list","name","non_ssl_bypass_service_group","notafter","notafterday","notaftermonth","notafteryear","notbefore","notbeforeday","notbeforemonth","notbeforeyear","ocsp_stapling","ocspst_ca_cert","ocspst_ocsp","ocspst_sg","ocspst_sg_days","ocspst_sg_hours","ocspst_sg_minutes","ocspst_sg_timeout","ocspst_srvr","ocspst_srvr_days","ocspst_srvr_hours","ocspst_srvr_minutes","ocspst_srvr_timeout","renegotiation_disable","req_ca_lists","server_name_auto_map","server_name_list","session_cache_size","session_cache_timeout","session_ticket_lifetime","sni_enable_log","ssl_false_start_disable","ssli_logging","sslilogging","sslv2_bypass_service_group","starts_with_list","template_cipher","template_hsm","user_tag","uuid","verify_cert_fail_action","version","web_category",]

__opts__ = salt.config.minion_config('/etc/salt/minion')
__grains__ = salt.laoder.grain(__opts__)


ret = dict(
    name="a10_slb_template_client_ssl",
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
    url_base = "/axapi/v3/slb/template/client-ssl/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)

def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/template/client-ssl/{name}"
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
    payload = build_json("client-ssl", kwargs)
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
    payload = build_json("client-ssl", kwargs)
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