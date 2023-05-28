from helpers.constants import PRIMITIVE_TYPES, TYPE_MAPPING, XML, XML_ITEM
from helpers.functions import get_items, get_key


class XMLSerializer:
    def dumps(self, obj) -> str:
        if type(obj) in PRIMITIVE_TYPES:
            obj_type = get_key(type(obj), TYPE_MAPPING)
            return f'<primitive type="{obj_type}">{obj}</primitive>'

        return XML.format(
            type=get_key(type(obj), TYPE_MAPPING) if type(obj) in TYPE_MAPPING.values() else "object",
            id=id(obj),
            items=self._load_to_xml(get_items(obj))
        )

    def _load_to_xml(self, obj: dict) -> str:
        xml_format = ""

        for k, v in obj.items():
            xml_format += f"\t{XML_ITEM.format(key=self.dumps(k), value=self.dumps(v))}"
        return xml_format
