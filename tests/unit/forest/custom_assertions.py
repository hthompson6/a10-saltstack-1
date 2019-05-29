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


class CustomAssertions(object):

    def _checkObjEquality(self, expected, actual):
        '''
        Assert that the attributes of the actual object
        equals the attributes of the expected. Not concerned with
        the object identities matching.
        '''

        # Compare id's
        if self.id != node.id:
            raise AssertionError('ObjNodes are not equal')
    
        if self.parent != node.parent:
            raise AssertionError('ObjNodes are not equal')
    
        if len(self.children) != len(node.children):
            raise AssertionError('ObjNodes are not equal')
    
        # Compare children node -> self
        for i in range(0, len(node.children)):
            if node.children[i] != self.children[i]:
                raise AssertionError('ObjNodes are not equal')
    
        # Compare children self -> node
        for i in range(0, len(self.children)):
            if self.children[i] != node.children[i]:
                raise AssertionError('ObjNodes are not equal')
    
        # Compare object values node -> self
        for k,v in self.val_dict:
            if self.node.val_dict.get(k) !=  self.val_dict[k]:
                raise AssertionError('ObjNodes are not equal')
    
        # Compare object values self -> node
        for k,v in self.val_dict:
            if self.val_dict[k] != self.node.val_dict.get(k):
                raise AssertionError('ObjNodes are not equal')


    def assertObjEquals(self, expected, actual):
        if isinstance(expected, list):
            if not isinstance(actual, list):
                raise AssertionError('Expected: {}, Actual: {}'.format(expected, actual))

            if len(expected) != len(actual):
                raise AssertionError('Expected: {}, Actual: {}'.format(expected, actual))

            for i in range(0, len(expected)):
                self._checkObjEquality(expected[i], actual[i])
        else:
            self._checkObjEquality(expected, actual)
