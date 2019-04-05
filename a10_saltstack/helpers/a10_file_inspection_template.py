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
    "bad_downloads_action",
    "bad_uploads_action",
    "downloads_bad_log",
    "downloads_external_inspect",
    "downloads_external_suspect_log",
    "downloads_good_log",
    "downloads_suspect_log",
    "good_downloads_action",
    "good_uploads_action",
    "inspect",
    "a10_name",
    "suspect_downloads_action",
    "suspect_uploads_action",
    "uploads_bad_log",
    "uploads_external_inspect",
    "uploads_external_suspect_log",
    "uploads_good_log",
    "uploads_suspect_log",
    "user_tag",
    "uuid",
]

REF_PROPERTIES = {
    "downloads_external_inspect": "/axapi/v3/slb/template/respmod-icap",
    "uploads_external_inspect": "/axapi/v3/slb/template/reqmod-icap",
}

MODULE_NAME = "template"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/file-inspection/template/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/file-inspection/template/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["a10-name"]

    return url_base.format(**f_dict)