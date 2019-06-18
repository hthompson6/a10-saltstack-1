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
        sess = Session(Mock(), 'good_user', 'good_pass')
        sess.id
        mock_auth.assert_called_with('good_user', 'good_pass')

    def test_authenticate_accepted(self):
        pass

    def test_authenticate_rejected(self):
        pass

    def test_close_no_sessid(self):
        pass

    def test_close_authorized(self):
        pass

    def test_close_unuathorized(self):
        pass
