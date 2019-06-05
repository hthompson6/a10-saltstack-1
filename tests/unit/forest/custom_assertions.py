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

from a10_saltstack.forest.nodes import ObjNode, InterNode


class CustomAssertions(object):

    def _get_id(self, node):
        if hasattr(node, 'id'):
            return node.id 
        elif hasattr(node, 'ref'):
            return node.ref

    def _checkGeneralEquality(self, expected, actual):
        '''
        Assert that the attributes of the actual object
        equals the attributes of the expected. Not concerned with
        the object identities matching.

        Classically, a general not equal assertion error would be raised.
        Given the number of potential inequalites that could arise in
        a failure, an extra layer of verbosity has been included.
        '''
        reason = ''

        if expected.parent != actual.parent:
            reason += ': Expected parent \'{}\' != ' \
                'Actual parent \'{}\''.format(
                expected.parent, actual.parent)

        equal_length = True    
        if len(expected.children) != len(actual.children):
            reason += ': Expected child list length \'{}\'' \
                ' != Actual child list length \'{}\''.format(
                len(expected.children), len(actual.children))
            equal_length = False

        # Need to compare lists which are spawned off dictionary.
        # So convert them back to dictionary.
        actual_dict = {}
        expected_dict = {}

        for child in actual.children:
            actual_dict[self._get_id(child)] = child

        for child in expected.children:
            expected_dict[self._get_id(child)] = child

        for k in expected_dict.keys():
            if expected_dict[k] !=  actual_dict.get(k):
                reason += ': Child node with identifier \'{}\' of ' \
                          'expected does not match actual'.format(k)
                break

        # One dict could be a proper subset of the other. 
        # To ensure that this isn't the case, a lenght check is done.
        if len(expected.val_dict) != len(actual.val_dict):
            reason += ': Expected val_dict length \'{}\'' \
                ' != Actual val_dict length \'{}\''.format(
                len(expected.val_dict), len(actual.val_dict))
            equal_length = False


        # Compare object values expected -> actual
        for k in expected.val_dict.keys():
            if expected.val_dict[k] != actual.val_dict.get(k):
                reason += ': val_dict key \'{}\' in expected was not' \
                          'found in the actual val_dict'.format(k)
                break

        return reason

    def _checkObjEquality(self, expected, actual):
        reason = ''

        if expected.id != actual.id:
            reason = ': Expected id \'{}\' != ' \
                     'Actual id \'{}\''.format(expected.id, actual.id)
        reason += self._checkGeneralEquality(expected, actual)

        if reason:
            raise AssertionError('Expected does not equal actual{}'.format(reason))

    def _checkInterEquality(self, expected, actual):
        reason = ''

        if expected.ref != actual.ref:
            reason = ': Expected ref \'{}\' != ' \
                     'Actual ref \'{}\''.format(expected.ref, actual.ref)
        reason += self._checkGeneralEquality(expected, actual)

        if reason:
            raise AssertionError('Expected does not equal actual{}'.format(reason))

    def _callAssertionCheck(self, expected, actual):
        # InterNode has to be checked first as it inherits from ObjNode
        if isinstance(expected, InterNode):
            if isinstance(actual, InterNode):
                self._checkInterEquality(expected, actual)
            else:
                raise AssertionError('Expected: {}, Actual: {}'.format(expected, actual))
        # If the expected is an ObjNode, but the actual is an InterNode
        elif isinstance(actual, InterNode):
             raise AssertionError('Expected: {}, Actual: {}'.format(expected, actual))
        elif isinstance(expected, ObjNode) and isinstance(actual, ObjNode):
            self._checkObjEquality(expected, actual)
        else:
            raise Exception('Provided arguments are not of correct type')

    def assertObjEquals(self, expected, actual):
        if isinstance(expected, list):
            if not isinstance(actual, list):
                raise AssertionError('Expected: {}, Actual: {}'.format(expected, actual))
            if len(expected) != len(actual):
                raise AssertionError('Expected: {}, Actual: {}'.format(expected, actual))

            # Need to compare lists which are spawned off dictionary.
            # So convert them back to dictionary.
            actual_dict = {}
            expected_dict = {}

            for node in actual:
                actual_dict[self._get_id(node)] = node

            for node in expected:
                expected_dict[self._get_id(node)] = node

            for k in expected_dict.keys():
                if expected_dict.get(k) and actual_dict.get(k):
                    self._callAssertionCheck(expected_dict[k], actual_dict[k])
                else:
                    raise AssertionError('Expected: {}, Actual: {}'.format(expected, actual))
        else:
            self._callAssertionCheck(expected[i], actual[i])
