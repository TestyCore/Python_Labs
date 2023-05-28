from helpers.constants import JSON, BOOL_TYPE, TYPE_MAPPING, JSON_TYPE
from helpers.functions import get_items, get_key, to_number
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

    def loads(self, json: str):
        if not len(json):
            return

        if json == ' ':
            return ...
        if json.startswith('"'):
            return json.strip('"')
        if json in BOOL_TYPE.values():
            return get_key(json, BOOL_TYPE)
        if to_number(json) is not None:
            return to_number(json)

