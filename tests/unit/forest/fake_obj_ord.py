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

from collections import OrderedDict


class BaseObject(OrderedDict):
    def __init__(self):
        super(BaseObject, self).__init__()


class FakeVirtualServer(BaseObject):
    def __init__(self):
        super(BaseObject, self).__init__()
        self['a10_name'] = 'VS2'
        self['service_group'] = FakeServiceGroup()


class FakeServiceGroup(BaseObject):
    def __init__(self):
        super(BaseObject, self).__init__()
        self['sg1'] = 'method'


class FakePort(BaseObject):
    def __init__(self, port_number):
        super(BaseObject, self).__init__()
        self[port_number] = OrderedDict([('protocol', 'tcp')])


class FakeMember(BaseObject):
    def __init__(self, port_number):
        super(BaseObject, self).__init__()
        self[port_number] = OrderedDict([('protocol', 'tcp')])
