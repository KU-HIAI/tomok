import importlib.util
from datetime import datetime


COLORED_TEXT = {
    'r': '\033[31m',
    'g': '\033[32m',
    'y': '\033[33m',
    'b': '\033[34m',
    'w': '\033[37m',
    'r+': '\033[91m',
    'g+': '\033[92m',
    'y+': '\033[93m',
    'b+': '\033[94m',
    'w+': '\033[97m',
}

COLORED_BG = {
    'r': '\033[41m',
    'g': '\033[42m',
    'y': '\033[43m',
    'b': '\033[44m',
    'r+': '\033[101m',
    'g+': '\033[102m',
    'y+': '\033[103m',
    'b+': '\033[104m',

}


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


def _get_timestamp_fstr() -> str:
    return datetime.now().strftime("%y-%m-%d %H:%M:%S")


def logging_warn(content: str, tag: str = "WARNING") -> None:
    colored_text = COLORED_TEXT['r+']
    clean = "\033[0m"
    timestamp: str = _get_timestamp_fstr()
    print(colored_text + f'[ {timestamp} ] {tag}: {content}' + clean)


def logging_system(content: str, tag: str = "") -> None:
    colored_text = COLORED_TEXT['y+']
    clean = "\033[0m"
    timestamp: str = _get_timestamp_fstr()
    print(colored_text + f'[ {timestamp} ] {tag}: {content}' + clean)


def logging_clear(content: str, tag: str = "") -> None:
    colored_text = COLORED_TEXT['g+']
    clean = "\033[0m"
    timestamp: str = _get_timestamp_fstr()
    print(colored_text + f'[ {timestamp} ] {tag}: {content}' + clean)


def logging_info(content: str, tag: str = "") -> None:
    colored_text = COLORED_TEXT['b+']
    clean = "\033[0m"
    timestamp: str = _get_timestamp_fstr()
    print(colored_text + f'[ {timestamp} ] {tag}: {content}' + clean)


def logging_normal(content: str, tag: str = "") -> None:
    colored_text = COLORED_TEXT['w+']
    clean = "\033[0m"
    timestamp: str = _get_timestamp_fstr()
    print(colored_text + f'[ {timestamp} ] {tag}: {content}' + clean)


if __name__ == "__main__":
    logging_system("test\nSLAB:\n- A24G3141\n- A24G3141\n- A24G3141")
