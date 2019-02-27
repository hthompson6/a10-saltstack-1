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

import a10_saltstack
import importlib

oper_enum = ['create', 'update', 'delete']


def get_url(a10_obj, oper, **kwargs):
    if oper not in oper_enum:
        return None

    obj_module = importlib.import_module(
        'a10_saltstack.helpers.a10_{}'.format(a10_obj.replace('-', '_')))

    if oper != 'create':
        return obj_module.existing_url(**kwargs)
    else:
        return obj_module.new_url(**kwargs)


def get_props(a10_obj, **kwargs):
    obj_module = importlib.import_module(
        'a10_saltstack.helpers.a10_{}'.format(a10_obj.replace('-', '_')))
 
    return obj_module.AVAILABLE_PROPERTIES


def get_obj_type(a10_obj):
    obj_module = importlib.import_module(
        'a10_saltstack.helpers.a10_{}'.format(a10_obj.replace('-', '_')))

    return obj_module.MODULE_NAME
