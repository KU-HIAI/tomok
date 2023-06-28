import importlib.util


def typename(obj):
    """
    Get the typename of object.

    :param obj: Target object.
    :return: Typename of the obj.
    """
    if not isinstance(obj, type):
        obj = obj.__class__
    try:
        return f'{obj.__module__}.{obj.__name__}'
    except AttributeError:
        return str(obj)


def import_check(module_name):
    if importlib.util.find_spec(module_name):
        return True
    else:
        print(f'{module_name} is not installed. ex) pip install {module_name}')
        return False