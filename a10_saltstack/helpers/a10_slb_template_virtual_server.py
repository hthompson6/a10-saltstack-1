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
AVAILABLE_PROPERTIES = ["conn_limit","conn_limit_no_logging","conn_limit_reset","conn_rate_limit","conn_rate_limit_no_logging","conn_rate_limit_reset","icmp_lockup","icmp_lockup_period","icmp_rate_limit","icmpv6_lockup","icmpv6_lockup_period","icmpv6_rate_limit","name","rate_interval","subnet_gratuitous_arp","tcp_stack_tfo_active_conn_limit","tcp_stack_tfo_backoff_time","tcp_stack_tfo_cookie_time_limit","user_tag","uuid",]

MODULE_NAME = 'virtual-server'

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/template/virtual-server/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/template/virtual-server/{name}"
    f_dict = {}
    f_dict["name"] = module.params["name"]

    return url_base.format(**f_dict)