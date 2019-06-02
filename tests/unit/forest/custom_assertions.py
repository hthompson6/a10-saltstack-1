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

        Classically, a general not equal assertion error would be raised.
        Given the number of potential inequalites that could arise in
        a failure, an extra layer of verbosity has been included.
        '''
        reason = ''

        # Compare id's
        if expected.id != actual.id:
            reason = ': ID Mismatch'
    
        if expected.parent != actual.parent:
            reason += ': Parents Are Not Equal'

        equal_length = True    
        if len(expected.children) != len(actual.children):
            reason += ': Length Mismatch'
            equal_length = False

        if equal_length:
            children_equal = True
            # Compare children actual -> expected
            for i in range(0, len(actual.children)):
                if actual.children[i] != expected.children[i]:
                    reason += ': Children Mismatch'
                    children_equal = False
                    break

            if children_equal:
                # Compare children expected -> actual
                for i in range(0, len(expected.children)):
                    if expected.children[i] != actual.children[i]:
                        reason += ': Children Mismatch' 
                        break
   
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

        if reason:
            raise AssertionError('Expected does not equal actual{}'.format(reason))


    def assertObjEquals(self, expected, actual):
        import pdb; pdb.set_trace()
        if isinstance(expected, list):
            if not isinstance(actual, list):
                raise AssertionError('Expected: {}, Actual: {}'.format(expected, actual))

            if len(expected) != len(actual):
                raise AssertionError('Expected: {}, Actual: {}'.format(expected, actual))

            for i in range(0, len(expected)):
                self._checkObjEquality(expected[i], actual[i])
        else:
            self._checkObjEquality(expected, actual)
