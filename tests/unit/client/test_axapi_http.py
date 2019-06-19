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

from a10_saltstack.client.axapi_http import HttpClient 


def TestAxapiHTTPClient(unittest.TestCase):

    def test_axapi_args_provided(self):
        pass

    @patch.object(HttpClient, '__init__')
    def test_file_name_unpopulated(self):
        with self.assertRaises(ValueError) as context:
            HttpClient()

    def test_file_content_unpopulated(self):
        pass

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
