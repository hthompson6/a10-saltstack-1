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

from mock import Mock, patch
import unittest

import errno
from a10_saltstack.client.axapi_http import HttpClient 


class TestAxapiHTTPClient(unittest.TestCase):

    def _patch_wrap(self, path):
        path_patcher = patch(path)
        ret = path_patcher.start()
        self.addCleanup(path_patcher.stop)
        return ret

    def setUp(self):
        dep_list = ['errno.errorcode', ]
        self.req_mock = self._patch_wrap('requests.request')
        self.json_mock = self._patch_wrap('json.dumps')
        self.resp_mock = self._patch_wrap('a10_saltstack.client.responses')
        self._patch_wrap('errno.errorcode')

    @patch.object(HttpClient, 'merge_dicts')
    def test_axapi_args_provided(self, merge_mock):
        test_axapi_args = {'fake_key': 'fake_val'}
        test_params = {'fake-key': 'fake-val'}
        HttpClient('1.1.1.1').request(Mock(), '/calm/down/morty', axapi_args=test_axapi_args,
            params=test_params)
        merge_mock.assert_called_with()

    def test_file_name_unpopulated(self):
        with self.assertRaises(ValueError) as context:
            HttpClient('1.1.1.1').request(Mock(), '/calm/down/morty', file_content=Mock())

    def test_file_content_unpopulated(self):
        with self.assertRaises(ValueError) as context:
            HttpClient('1.1.1.1').request(Mock(), '/calm/down/morty', file_name=Mock())

    def test_socket_error(self):
        pass

    def test_connection_error(self):
        pass

    def test_data_request(self):
        pass

    def test_file_request(self):
        pass

    def test_json_resp_value_error_200(self):
        pass

    def test_json_resp_value_error(self):
        pass

    def test_raise_axapi_ex(self):
        pass

    def test_raise_axapi_auth(self):
        pass
