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


def _ret_ops(a10_obj, post_result):
    ret = dict(
        name=a10_obj,
        changes={},
        original_message="",
        result=False,
        comment=""
    )

    ret["changes"].update(**post_result.get('post_resp', {}))
    if  post_result.get('post_resp'):
        del post_result['post_resp']
    ret.update(post_result)

    return ret


def create(**kwargs):
    a10_obj = kwargs['a10_obj']
    del kwargs['a10_obj']
    post_result = __salt__['a10.create'](a10_obj, **kwargs) 
    return _ret_ops(a10_obj, post_result)  

 
def update(**kwargs):
    a10_obj = kwargs['a10_obj']
    del kwargs['a10_obj']
    post_result = __salt__['a10.update'](a10_obj, **kwargs)
    return _ret_ops(a10_obj, post_result) 


def delete(**kwargs):
    a10_obj = kwargs['a10_obj']
    del kwargs['a10_obj']
    post_result = __salt__['a10.delete'](a10_obj, **kwargs)
    return _ret_ops(a10_obj, post_result) 
