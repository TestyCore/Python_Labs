from helpers.constants import JSON, BOOL_TYPE, TYPE_MAPPING
from helpers.functions import get_items
from helpers.jsonformat import JSONFormat


class JSONSerializer:

    def dumps(self, obj) -> str:
        if type(obj) == str:
            return f'"{obj}"'
        if type(obj) in (int, float, complex):
            return str(obj)
        if type(obj) in [bool, type(None)]:
            return BOOL_TYPE[obj]

        return JSON.format(
            type=type(obj) if type(obj) in TYPE_MAPPING.values() else object,
            id=id(obj),
            items=JSONFormat.to_json(get_items(obj), self.dumps)
        )

