import a10_saltstack

oper_enum = ['create', 'update', 'delete']

def get_url(oper, **kwargs):
    if oper not in oper_enum:
        return None

    a10_obj = kwargs['a10_obj']
    del kwargs['a10_obj']
    obj_module = __import__('a10_saltstack.helpers.a10_' + str(a10_obj).replace('-', '_'))

    if oper != 'create':
        return obj_module.existing_url(**kwargs)
    else:
        return obj_module.new_url(**kwargs)

def get_props(**kwawrgs):
    a10_obj = kwargs['a10_obj']
    obj_module = getattr(a10_saltstack, 'a10_' + str(a10_obj).replace('-', '_'))
    return obj_module.AVAILABLE_PROPERTIES
