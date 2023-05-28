from types import LambdaType


from types import FunctionType, MethodType, CodeType, ModuleType, CellType


JSON = ('''{{
    "{type}_{id:x}": {{
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

IGNORED_FIELDS: set[str] = {
        '__weakref__',
        '__subclasshook__',
        '__dict__',
        '__doc__'
}
IGNORED_FIELD_TYPES: set[str] = {
    'BuiltinFunctionType', 'BuiltinMethodType',
    'WrapperDescriptorType', 'MethodDescriptorType',
    'MappingProxyType', 'GetSetDescriptorType',
    'MemberDescriptorType'
}

