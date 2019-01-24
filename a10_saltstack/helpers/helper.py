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
        return obj_module.new_url()

def get_props(a10_obj, **kwargs):
    obj_module = importlib.import_module(
        'a10_saltstack.helpers.a10_{}'.format(a10_obj.replace('-', '_')))
 
    return obj_module.AVAILABLE_PROPERTIES
