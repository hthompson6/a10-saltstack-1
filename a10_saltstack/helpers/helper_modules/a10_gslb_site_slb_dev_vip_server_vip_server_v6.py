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
AVAILABLE_PROPERTIES = ["ipv6","sampling_enable","uuid","slb_dev_device_name","site_name",]

REF_PROPERTIES = {
}

MODULE_NAME = "vip-server-v6"

PARENT_KEYS = ["slb_dev_device_name","site_name",]

CHILD_KEYS = ["ipv6",]


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/gslb/site/{site_name}/slb-dev/{slb_dev_device_name}/vip-server/vip-server-v6/{ipv6}"
    f_dict = {}
    f_dict["ipv6"] = ""
    f_dict["slb_dev_device_name"] = kwargs["slb_dev_device_name"]
    f_dict["site_name"] = kwargs["site_name"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/gslb/site/{site_name}/slb-dev/{slb_dev_device_name}/vip-server/vip-server-v6/{ipv6}"
    f_dict = {}
    f_dict["ipv6"] = kwargs["ipv6"]
    f_dict["slb_dev_device_name"] = kwargs["slb_dev_device_name"]
    f_dict["site_name"] = kwargs["site_name"]

    return url_base.format(**f_dict)