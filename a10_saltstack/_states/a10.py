#!/usr/bin/python

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import salt
import salt.config


def _ret_ops(a10_obj, post_result):
    ret = dict(
        name=kwargs['a10_obj'],
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
    post_result = __salt__['a10.create'](a10_obj, **kwargs) 
    return _ret_ops(a10_obj, post_result)  

 
def update(**kwargs):
    a10_obj = kwargs['a10_obj']
    post_result = __salt__['a10.update'](a10_obj, **kwargs)
    return _ret_ops(a10_obj, post_result) 


def delete(**kwargs):
    a10_obj = kwargs['a10_obj']
    post_result = __salt__['a10.delete'](a10_obj, **kwargs)
    return _ret_ops(a10_obj, post_result) 
