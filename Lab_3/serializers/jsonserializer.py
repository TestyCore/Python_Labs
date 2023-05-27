from helpers.constants import JSON, BOOL_TYPE, TYPE_MAPPING


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
            items=self.formatter.to_json(self.get_items(obj), self.dumps)
        )

