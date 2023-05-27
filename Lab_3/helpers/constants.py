from types import (
    FunctionType, LambdaType, MethodType,
    CodeType, CellType, ModuleType
)

JSON = ('''{{ "{type}_{id:x}": {{
    {items}
    }}
}}''')

JSON_TYPE: str = r"<class '(\w\S+)'>_"

PRIMITIVE_TYPES: tuple = (int, float, complex, str, bool, type(None))

BOOL_TYPE: dict[bool, str] = {
        None: 'null',
        True: 'true',
        False: 'false'
    }

TYPE_MAPPING = {
    'int': int,
    'float': float,
    'complex': complex,
    'str': str,
    'bool': bool,
    'NoneType': type(None),
    'bytes': bytes,
    'list': list,
    'tuple': tuple,
    'set': set,
    'dict': dict,
    'code': CodeType,
    'cell': CellType,
    'function': FunctionType,
    'lambda': LambdaType,
    'method': MethodType,
    'staticmethod': staticmethod,
    'classmethod': classmethod,
    'type': type,
    'module': ModuleType,
    'object': object,
}

