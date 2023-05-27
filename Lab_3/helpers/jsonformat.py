from helpers.constants import PRIMITIVE_TYPES


class JSONFormat:

    @staticmethod
    def to_json(obj: dict, dumps):
        json_format = ""

        for k, v in obj.items():
            if type(v) in PRIMITIVE_TYPES:
                json_format += f"\t{dumps(k)}: {dumps(v)},\n"
                continue

            json_format += f"\t{dumps(k)}: {{\n"

            for line in dumps(v).split("\n")[1:]:
                json_format += f"\t{line}\n"

        return json_format
