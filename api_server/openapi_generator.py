from tomok import RuleUnitController
import re
import inspect
from ruamel.yaml import YAML

def dict_generator(indict, pre=None):
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                for d in dict_generator(value, pre + [key]):
                    yield d
            elif isinstance(value, list) or isinstance(value, tuple):
                for v in value:
                    for d in dict_generator(v, pre + [key]):
                        yield d
            else:
                yield pre + [key, value]
    else:
        yield pre + [indict]


def _find_docstring_variables(func):
    """Find variables in the given function's docstring."""
    docstring = inspect.getdoc(func)

    # Define regex patterns for args and variable names/descriptions
    arg_pattern = re.compile(r"Args:\n(.+?)(\n\n|$)", re.S)
    return_pattern = re.compile(r"Returns:\n(.+?)(\n\n|$)", re.S)
    var_pattern = re.compile(r"(\w+)\s\(([\w.]+)\):(.+)")

    arg_block_match = arg_pattern.search(docstring)
    return_block_match = return_pattern.search(docstring)

    if arg_block_match and return_block_match:
        arg_block = arg_block_match.group(1)
        arg_vars = var_pattern.findall(arg_block)
        return_block = return_block_match.group(1)
        return_vars = var_pattern.findall(return_block)

        # Remove leading/trailing white spaces from description.
        arg_vars = [(var[0], var[1], var[2].strip()) for var in arg_vars]
        return_vars = [(var[0], var[1], var[2].strip()) for var in return_vars]
        
        return arg_vars, return_vars
    else:
        return []

ruc = RuleUnitController('./ruleunits')
paths = {}

for std in dict_generator(ruc.ruleunits_dict):
    # print(len(std[-1].rule_methods))
    uri = std[0:-2]
    uri[0] = '/' + uri[0]
    uri.append(std[-1].rule_methods[0].fn.__name__)
    # print('/'.join(uri))
    uri_str = '/'.join(uri)
    tags = std[0]
    if type(tags) is not list:
        tags = [tags]
    operation_id = ['ruleunits'] + std[0:-1]
    operation_id.append(std[-1].rule_methods[0].fn.__name__)
    # print('.'.join(operation_id))
    operation_id_str = '.'.join(operation_id)
    # print(std[-1].title)
    args, return_args = _find_docstring_variables(std[-1].rule_methods[0].fn)
    args_dict = {}
    return_args_dict = {}
    type_conv = {
        'float': 'number',
        'int': 'integer',
        'integer': 'integer',
        'str': 'string',
        'bool': 'boolean',
        'string': 'string',
        'sting': 'string'
    }
    for arg in args:
        args_dict[arg[0]] = {
            'type': type_conv[arg[1]],
            'description': arg[2]
        }
    for arg in return_args:
        return_args_dict[arg[0]] = {
            'type': type_conv[arg[1]],
            'description': arg[2]
        }
    # print(std)
    docstr = inspect.getdoc(std[-1].rule_methods[0].fn)
    markdown = std[-1].content
    lines = markdown.split("\n")
    lines = [line for line in lines if line.strip() != '']
    if len(lines) > 0:
        if lines[0].startswith("    "):
            lines = [line[5:] for line in lines if line.startswith("    ")]
    markdown = '\n'.join(lines)
    mermaid = std[-1]._get_mermaid_ink_url(std[-1].flowchart)
    description = f"""{markdown}

![]({mermaid})

```
{docstr}
```
"""
    paths[uri_str] = {
        'post': {
            'summary': std[-1].title,
            'operationId': operation_id_str,
            'description': description,
            'tags': tags,
            'requestBody': {
                'content': {
                    'multipart/form-data': {
                        'schema': {
                            'type': 'object',
                            'properties': args_dict
                        }
                    }
                }
            },
            'responses': {
                '200': {
                    'description': 'Success response',
                    'content': {
                        'application/json': {
                            'schema': {
                                'type': 'object',
                                'properties': return_args_dict
                            }
                        }
                    }
                }
            },
            'security': [{
                'api_key': []
            }]
        }
    }

openapi_str = {}
openapi_str['openapi'] = '3.0.0'
openapi_str['info'] = {
    'title': 'TOMOK API',
    'version': '1.0'
}
openapi_str['servers'] = [
    {'url': 'https://tomok-dev.hiai.kr/v1.0'}
]
openapi_str['tags'] = [
    {'name':'default'},
    {'name':'kds', 'description': '설계기준(KDS)'},
    {'name':'kcs', 'description': '표준시방서(KCS)'}
]
secret_path = {'/secret': {
    'get': {
        'summary': 'Return secret string',
        'operationId': 'secret.get_secret',
        'responses': {
            '200': {
                'description': 'Success response',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'msg': {
                                    'type': 'string',
                                    'description': '실행 확인 / 오류 메시지'
                                }
                            }
                        }
                    }
                }
            }
        },
        'security': [{
            'api_key': []
        }]
    }
}}
openapi_str['paths'] = secret_path
openapi_str['paths'].update(paths)
openapi_str['components'] = {
    'securitySchemes': {
        'api_key': {
            'type': 'apiKey',
            'name': 'X-Auth',
            'in': 'header',
            'x-apikeyInfoFunc': 'secret.apikey_auth'
        }
    }
}
yaml_builder = YAML()
with open('./openapi/tomok-api.yaml', 'w') as fp:
    yaml_builder.dump(openapi_str, stream=fp)