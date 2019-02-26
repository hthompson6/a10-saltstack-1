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
AVAILABLE_PROPERTIES = ["admin_dn","admin_secret","auth_type","base","bind_with_dn","ca_cert","default_domain","derive_bind_dn","dn_attribute","encrypted","health_check","health_check_disable","health_check_string","host","ldaps_conn_reuse_idle_timeout","name","port","port_hm","port_hm_disable","prompt_pw_change_before_exp","protocol","pwdmaxage","sampling_enable","secret_string","timeout","uuid",]

MODULE_NAME = 'instance'

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/aam/authentication/server/ldap/instance/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/aam/authentication/server/ldap/instance/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["name"]

    return url_base.format(**f_dict)