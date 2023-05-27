from helpers.constants import BOOL_TYPE


class JSONSerializer:

    def dumps(self, obj) -> str:
        if type(obj) == str:
            return f'"{obj}"'
        if type(obj) in (int, float, complex):
            return str(obj)
        if type(obj) in [bool, type(None)]:
            return BOOL_TYPE[obj]

