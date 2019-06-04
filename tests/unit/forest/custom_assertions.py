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
        actual_dict = {}
        expected_dict = {}

        for child in actual.children:
            if hasattr(child, 'id'):
                actual_dict[child.id] = child
            elif hasattr(child, 'ref'):
                actual_dict[child.ref] = child

        for child in expected.children:
            if hasattr(child, 'id'):
                expected_dict[child.id] = child
            elif hasattr(child, 'ref'):
                expected_dict[child.ref] = child


        # One dict could be a proper subset of the other. 
        # As such, the check must be done in both directions.

        # Replace with length check
        val_dict_equal = True 

        # Compare object values actual -> expected
        for k in actual.val_dict.keys():
            if actual.val_dict[k] !=  expected.val_dict.get(k):
                reason += ': Value Dictionary Mismatch'
                val_dict_equal = False
                break 

        if val_dict_equal:
            # Compare object values expected -> actual
            for k in expected.val_dict.keys():
                if expected.val_dict[k] != actual.val_dict.get(k):
                    reason += ': Value Dictionary Mismatch'
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
            for i in range(0, len(expected)):
                self._callAssertionCheck(expected[i], actual[i])
        else:
            self._callAssertionCheck(expected[i], actual[i])
