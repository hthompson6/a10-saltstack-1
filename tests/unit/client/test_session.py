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

from a10_saltstack.client.session import Session


class TestSession(unittest.TestCase):

    @patch.object(Session, 'authenticate', auto_spec=True)
    def test_id_auth_called(self, mock_auth):
        Session(Mock(), 'good_user', 'good_pass').id
        mock_auth.assert_called_with('good_user', 'good_pass')

    @patch.object(Session, 'close', auto_spec=True)
    def test_authenticate_accepted(self, mock_close):
        auth_resp = {'authresponse': {'signature': 1337}}
        attrs = {'post.return_value': auth_resp}
        mock_http = Mock()
        mock_http.configure_mock(**attrs)
        sess = Session(mock_http, Mock(), Mock())
        sess.authenticate(Mock(), Mock())
        self.assertEquals('1337', sess.session_id)

    @patch.object(Session, 'close', auto_spec=True)
    def test_authenticate_rejected(self, mock_close):
        auth_resp = {'bad_resp': None}
        attrs = {'post.return_value': auth_resp}
        mock_http = Mock()
        mock_http.configure_mock(**attrs)
        sess = Session(mock_http, Mock(), Mock())
        sess.authenticate(Mock(), Mock())
        self.assertIsNone(sess.session_id)

    def test_close_no_sessid(self):
        mock_http = Mock()
        sess = Session(mock_http, Mock(), Mock())
        sess.close()

        mock_http.post.assert_not_called()

    def test_close_authorized(self):
        mock_http = Mock()
        sess = Session(mock_http, Mock(), Mock())    
        sess.session_id = '1337'
        sess.close()

        mock_http.post.assert_called_with('/axapi/v3/logoff', headers={'Authorization': 'A10 1337'})
