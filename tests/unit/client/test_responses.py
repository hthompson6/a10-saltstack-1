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

from a10_saltstack.client import responses as resp
from a10_saltstack.client import errors as ae


class TestResponses(unittest.TestCase):

    def test_auth_error_401(self):
        response = {'authorizationschema': {'code': 401, 'error': 'ni'}}
        with self.assertRaises(ae.AuthenticationFailure) as context:
            resp.raise_axapi_auth_error(response, Mock(), Mock(), None)

        self.assertTrue('401 ni' in str(context.exception))

    def test_auth_error_403(self):
        response = {'authorizationschema': {'code': 403, 'error': 'ni'}}
        with self.assertRaises(ae.AuthenticationFailure) as context:
            resp.raise_axapi_auth_error(response, Mock(), Mock(), None)
        
        self.assertTrue('403 ni' in str(context.exception)) 

    def test_auth_error_invalid_session_401(self):
        response = {'authorizationschema': {'code': 401, 'error': 'ni'}}
        headers = {'Authorization': 'A10 1234'}
        with self.assertRaises(ae.InvalidSessionID) as context:
            resp.raise_axapi_auth_error(response, Mock(), Mock(), headers)

        self.assertTrue('401 ni' in str(context.exception))

    def test_axapi_ex_no_response(self):
        response = {'response': {}}
        with self.assertRaises(ae.ACOSException) as context:
            resp.raise_axapi_ex(response, Mock(), Mock())

    def test_axapi_ex_unknown_code(self):
        response = {'response': {'err': {'code': 1234, 'msg': 'ni'}}}
        with self.assertRaises(ae.ACOSException) as context:
            resp.raise_axapi_ex(response, Mock(), Mock())

        self.assertTrue('1234 ni' in str(context.exception))

    def test_axapi_ex_http_method(self):
        response = {'response': {'err': {'code': 1023410176, 'msg': 'ni'}}}
        self.assertIsNone(resp.raise_axapi_ex(response, 'DELETE', Mock()))

    def test_axapi_ex_no_http_method(self):
        response = {'response': {'err': {'code': 1023410176, 'msg': 'ni'}}}
        with self.assertRaises(ae.NotFound) as context:
            resp.raise_axapi_ex(response, 'CREATE', Mock())

        self.assertTrue('1023410176 ni' in str(context.exception))

    def test_axapi_ex_match(self):
        response = {'response': {'err': {'code': 1023459339, 'msg': 'ni'}}}
        with self.assertRaises(ae.Exists) as context:
            resp.raise_axapi_ex(response, 'CREATE', '/axapi/v3/slb/server') 

        self.assertTrue('1023459339 ni' in str(context.exception))
