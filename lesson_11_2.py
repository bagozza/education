import inspect
from pprint import pprint


def introspection_info(obj):
    module = inspect.getmodule(introspection_info)
    attributes = []
    methods = []
    for i in dir(obj):
        if callable(getattr(obj, i)):
            methods.append(i)
        else:
            attributes.append(i)
    return {'type': type(obj),
            'attributes': attributes,
            'methods': methods,
            'module': module}


number_info = introspection_info(42)
pprint(number_info)
