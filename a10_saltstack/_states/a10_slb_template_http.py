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
AVAILABLE_PROPERTIES = ["http_100_cont_wait_for_req_complete","bypass_sg","client_ip_hdr_replace","client_port_hdr_replace","compression_auto_disable_on_high_cpu","compression_content_type","compression_enable","compression_exclude_content_type","compression_exclude_uri","compression_keep_accept_encoding","compression_keep_accept_encoding_enable","compression_level","compression_minimum_content_length","cookie_format","failover_url","host_switching","insert_client_ip","insert_client_ip_header_name","insert_client_port","insert_client_port_header_name","keep_client_alive","log_retry","name","non_http_bypass","persist_on_401","rd_port","rd_resp_code","rd_secure","rd_simple_loc","redirect","redirect_rewrite","req_hdr_wait_time","req_hdr_wait_time_val","request_header_erase_list","request_header_insert_list","request_line_case_insensitive","response_content_replace_list","response_header_erase_list","response_header_insert_list","retry_on_5xx","retry_on_5xx_per_req","retry_on_5xx_per_req_val","retry_on_5xx_val","strict_transaction_switch","template","term_11client_hdr_conn_close","url_hash_first","url_hash_last","url_hash_offset","url_hash_persist","url_switching","use_server_status","user_tag","uuid",]

__opts__ = salt.config.minion_config('/etc/salt/minion')
__grains__ = salt.laoder.grain(__opts__)


ret = dict(
    name="a10_slb_template_http",
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
    url_base = "/axapi/v3/slb/template/http/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)

def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/template/http/{name}"
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
    payload = build_json("http", kwargs)
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
    payload = build_json("http", kwargs)
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