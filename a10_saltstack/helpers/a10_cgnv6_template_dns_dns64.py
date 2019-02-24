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
AVAILABLE_PROPERTIES = ["answer_only_disable","auth_data","cache","change_query","compress_disable","deep_check_rr_disable","drop_cname_disable","enable","ignore_rcode3_disable","max_qr_length","parallel_query","passive_query_disable","retry","single_response_disable","timeout","trans_ptr","trans_ptr_query","ttl","uuid",]

MODULE_NAME = dns64

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/cgnv6/template/dns/{dns_name}/dns64"
    f_dict = {}
    f_dict["dns_name"] = module.params["dns_name"]

    return url_base.format(**f_dict)


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/cgnv6/template/dns/{dns_name}/dns64"
    f_dict = {}
    f_dict["dns_name"] = module.params["dns_name"]

    return url_base.format(**f_dict)