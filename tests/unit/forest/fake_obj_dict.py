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


class BaseObject(dict):
    def __init__(self):
        super(BaseObject, self).__init__()


class FakeVirtualServer(BaseObject):
    def __init__(self):
        super(BaseObject, self).__init__()
        self['ip_address'] = '192.168.4.2'

    def add_port(self, port_num):
        port = self.FakePort(port_num)
        if self.get('port_list'):
            self['port_list'].update({port_num: port})
        else:
            self['port_list'] = {port_num: port}

    def add_sg(self, sg_name):
        sg = self.FakeServiceGroup(sg_name)
        if self.get('service_group'):
            self['service_group'].update({sg_name: sg})
        else:
            self['service_group'] = {sg_name: sg}

class FakeServiceGroup(BaseObject):
    def __init__(self):
        super(BaseObject, self).__init__()
        self['lb_type'] = 'round_robin'

    def add_member(self, mem_name, host):
        mem = self.FakeMember(host)
        if self.get('member_list'):
            self['member_list'].update({mem_name: mem})
        else:
            self['member_list'] = {mem_name: mem}


class FakePort(BaseObject):
    def __init__(self, port_num):
        super(BaseObject, self).__init__()
        self[port_num] = {'protocol': 'tcp'}


class FakeMember(BaseObject):
    def __init__(self, host):
        super(BaseObject, self).__init__()
        self['host'] = host
        self['port'] = 80
