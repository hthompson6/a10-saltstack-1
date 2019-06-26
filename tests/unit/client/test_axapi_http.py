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

import errno
from mock import ANY, Mock, patch
import requests
import socket
import unittest

from a10_saltstack.client.axapi_http import HttpClient 


class TestAxapiHTTPClient(unittest.TestCase):

    def _patch_wrap(self, path):
        path_patcher = patch(path)
        ret = path_patcher.start()
        self.addCleanup(path_patcher.stop)
        return ret

    def setUp(self):
        dep_list = ['errno.errorcode', 'http.client']
        self.req_mock = self._patch_wrap('requests.request')
        self.json_mock = self._patch_wrap('json.dumps')
        self.resp_mock = self._patch_wrap('a10_saltstack.client.axapi_http.acos_responses')
        self._patch_wrap('errno.errorcode')
        self.api_url = '/calm/down/morty'
        self.host = '1.1.1.1'

    @patch.object(HttpClient, 'merge_dicts')
    def test_axapi_args_provided(self, merge_mock):
        test_axapi_args = {'fake_axapi_key': 'fake_val'}
        test_params = {'fake-param-key': 'fake-param-val'}
        HttpClient(self.host).request(Mock(), self.api_url, axapi_args=test_axapi_args,
            params=test_params)
        merge_mock.assert_called_with(test_params, {'fake-axapi-key': 'fake_val'})

    def test_file_name_unpopulated(self):
        with self.assertRaises(ValueError) as context:
            HttpClient(self.host).request(Mock(), self.api_url, file_content=Mock())

    def test_file_content_unpopulated(self):
        with self.assertRaises(ValueError) as context:
            HttpClient(self.host).request(Mock(), self.api_url, file_name=Mock())

    def test_socket_error(self):
        self.req_mock.side_effect = socket.error
        with self.assertRaises(socket.error) as context:
            HttpClient(self.host).request(Mock(), self.api_url)

    def test_connection_error(self):
        self.req_mock.side_effect = requests.exceptions.ConnectionError
        with self.assertRaises(requests.exceptions.ConnectionError) as context:
            HttpClient(self.host).request(Mock(), self.api_url)

    def test_data_request(self):
        test_params = {'fake-key': 'fake-val'}
        HttpClient(self.host).request(Mock(), self.api_url, params=test_params)
        self.req_mock.assert_called_with(ANY, ANY, data=self.json_mock(), headers=ANY, verify=ANY)

    def test_file_request(self):
        fake_file_name = 'takeshi_kovacs.envoy'
        fake_file_content = Mock()
        fake_files = {
            'file': (fake_file_name, fake_file_content, "application/octet-stream"),
            'json': ('blob', None, "application/json")
        }

        HttpClient(self.host).request(Mock(), self.api_url, file_name=fake_file_name,
            file_content=fake_file_content)
        self.req_mock.assert_called_with(ANY, ANY, files=fake_files, headers=ANY, verify=ANY)

    def test_json_resp_value_error_200(self):
        attrs = {'status_code': 200, 'json.side_effect': ValueError}
        self.req_mock.return_value = Mock(**attrs)
        resp = HttpClient(self.host).request(Mock(), self.api_url)

        self.assertEquals(resp, {})

    def test_json_resp_value_error(self):
        attrs = {'json.side_effect': ValueError}
        self.req_mock.return_value = Mock(**attrs)
        with self.assertRaises(ValueError) as context:
            HttpClient(self.host).request(Mock(), self.api_url)

    def test_raise_axapi_ex(self):
        fake_resp = {'response': {'status': 'fail'}}
        attrs = {'json.return_value': fake_resp}
        self.req_mock.return_value = Mock(**attrs)
        HttpClient(self.host).request(Mock(), self.api_url)

        self.resp_mock.raise_axapi_ex.assert_called()

    def test_raise_axapi_auth(self):
        fake_resp = {'authorizationschema': {'code': 401, 'error': 'ni'}}
        attrs = {'json.return_value': fake_resp}
        self.req_mock.return_value = Mock(**attrs)
        HttpClient(self.host).request(Mock(), self.api_url)

        self.resp_mock.raise_axapi_auth_error.assert_called()
