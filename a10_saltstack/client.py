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


class A10Client(object):
    def __init__(self, session):
        self.session = session

    def _request(self, method, url, params, **kwargs):
        try:
            return self.session.http.request(method, url, params,
                                            self.session.get_auth_header(), **kwargs)
        except (ae.InvalidSessionID) as e:
            raise e

    def get(self, url, params={}, **kwargs):
        return self._request('GET', url, params, **kwargs)

    def post(self, url, params={}, **kwargs):
        return self._request('POST', url, params, **kwargs)

    def put(self, url, params={}, **kwargs):
        return self._request('PUT', url, params, **kwargs)

    def delete(self, url, params={}, **kwargs):
        return self._request('DELETE', url, params, **kwargs)
