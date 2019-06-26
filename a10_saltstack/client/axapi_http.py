# Copyright 2018,  A10 Networks.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


import errno
import json
import logging
import requests
import socket
import sys
import time

from a10_saltstack.client import errors as ae
from a10_saltstack.client import responses as acos_responses
import http.client as http_client


LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)

broken_replies = {
    "": '{"response": {"status": "OK"}}'
}


class HttpClient(object):
    HEADERS = {
        "Content-type": "application/json",
        "User-Agent": "a10-saltstack"
    }

    def __init__(self, host, port=None, protocol="https", timeout=None,
                 retry_errno_list=None):
        if port is None:
            if protocol is 'http':
                port = 80
            else:
                port = 443
        self.url_base = "%s://%s:%s" % (protocol, host, port)
        self.retry_errnos = []
        if retry_errno_list is not None:
            self.retry_errnos += retry_errno_list
        self.retry_err_strings = (['BadStatusLine'] +
                                  ['[Errno %s]' % n for n in self.retry_errnos] +
                                  [errno.errorcode[n] for n in self.retry_errnos
                                   if n in errno.errorcode])

    def request(self, method, api_url, params={}, headers=None,
                file_name=None, file_content=None, axapi_args=None, **kwargs):
        '''
        Preforms HTTP/HTTPS requests against the AXAPI.

        Args:
            method (string): POST/GET/PUT/DELETE
            api_url (string): API endpoint
            **kwargs: arbitrary keyword arguments

        Kwargs:
            params (dict): payload
            headers (dict): HTTP headers
            file_name (string): name of the file for ftp
            file_contents (object): file to be uploaded
            axapi_args (dict): extra axapi arguments

        Returns (dict):
            JSON response from the AXAPI
        '''
        LOG.debug("axapi_http: full url = %s", self.url_base + api_url)
        LOG.debug("axapi_http: %s url = %s", method, api_url)

        # Update params with axapi_args for currently unsupported configuration of objects
        if axapi_args is not None:
            formatted_axapi_args = dict([(k.replace('_', '-'), v) for k, v in
                                        axapi_args.items()])
            params = self.merge_dicts(params, formatted_axapi_args)

        if (file_name is None and file_content is not None) or \
           (file_name is not None and file_content is None):
            raise ValueError("file_name and file_content must both be "
                             "populated if one is")

        hdrs = self.HEADERS.copy()
        if headers:
            hdrs.update(headers)

        if params:
            params_copy = params.copy()
            payload = json.dumps(params_copy)
        else:
            payload = None

        if file_name is not None:
            files = {
                'file': (file_name, file_content, "application/octet-stream"),
                'json': ('blob', payload, "application/json")
            }

            hdrs.pop("Content-type", None)
            hdrs.pop("Content-Type", None)

        last_e = None

        try:
            last_e = None
            if file_name is not None:
                z = requests.request(method, self.url_base + api_url, verify=False,
                                        files=files, headers=hdrs)
            else:
                z = requests.request(method, self.url_base + api_url, verify=False,
                                        data=payload, headers=hdrs)
        except (socket.error, requests.exceptions.ConnectionError) as e:
            raise e

        if z.status_code == 204:
            return None

        try:
            r = z.json()
        except ValueError as e:
            if z.status_code == 200:
                return {}
            else:
                raise e

        if 'response' in r and 'status' in r['response']:
            if r['response']['status'] == 'fail':
                    acos_responses.raise_axapi_ex(r, method, api_url)

        if 'authorizationschema' in r:
            acos_responses.raise_axapi_auth_error(
                r, method, api_url, headers)

        return r

    def merge_dicts(self, d1, d2):
        d = d1.copy()
        for k, v in d2.items():
            if k in d and isinstance(d[k], dict):
                d[k] = self.merge_dicts(d[k], d2[k])
            else:
                d[k] = d2[k]
        return d


    def get(self, api_url, params={}, headers=None, **kwargs):
        return self.request("GET", api_url, params, headers, **kwargs)

    def post(self, api_url, params={}, headers=None, **kwargs):
        return self.request("POST", api_url, params, headers, **kwargs)

    def put(self, api_url, params={}, headers=None, **kwargs):
        return self.request("PUT", api_url, params, headers, **kwargs)

    def delete(self, api_url, params={}, headers=None, **kwargs):
        return self.request("DELETE", api_url, params, headers, **kwargs)
