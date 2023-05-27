JSON_TYPE: str = r"<class '(\w\S+)'>_"

PRIMITIVE_TYPES: tuple = (int, float, complex, str, bool, type(None))

BOOL_TYPE: dict[bool, str] = {
        None: 'null',
        True: 'true',
        False: 'false'
    }

JSON = ('''{{ "{type}_{id:x}": {{
    {items}
    }}
}}''')
