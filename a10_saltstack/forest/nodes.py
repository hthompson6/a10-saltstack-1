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


class ObjNode(object):

    def __init__(self, id, **kwargs):
        self.id = id

        self.parent = None
        self.children = []
        self.val_dict = kwargs

    def addParent(self, parent):
        self.parent = parent

    def addChild(self, child):
        child.addParent(self)
        self.children.append(child)


class RootNode(ObjNode):

    def __init__(self, id, ref):
        self.ref = ref
        self.id = id

        self.parent = None
        self.children = []
        self.val_dict = {}

    def addValDict(**kwargs):
        self.val_dict = kwargs


class InterNode(ObjNode):

    def __init__(self, key, ref):
        self.parent = None
        self.children = []
        self.ref = ref

        if key[-5:] == '-list':
            self.key = key[:-5]
        else:
            self.key = key
