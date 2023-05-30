import argparse
from typing import Any

from serializers.jsonserializer import JSONSerializer
from serializers.xmlserializer import XMLSerializer


class User:

    def __init__(self, username: str):
        self.username = username

    def change(self):
        self.username = "Anton"

    def pri(self):
        print("Vorontsov")

    def __repr__(self):
        return f"User('{self.username}')"

    def __str__(self):
        return f"Username - {self.username}"


def main():
    # a = User("slava")
    # # print(type(a))
    # # print(a.__str__())
    # # print(repr(a))
    # # a = [1, 2, 5]
    # json = JSONSerializer()
    # b = json.dumps(a)
    # c = json.loads(b)
    #
    # c.change()
    # # print(c.name) Error
    # print(c)
    # c.pri()


    # xml = XMLSerializer()
    # b = xml.dumps(a)
    # c = xml.loads(b)
    #
    # c.change()
    # print(c.username)
    # c.pri()

    parser = argparse.ArgumentParser()
    parser.add_argument('file_from')
    parser.add_argument('file_to')
    parser.add_argument('format_from')
    parser.add_argument('format_to')

    args = parser.parse_args()
    file_from, file_to, format_from, format_to = (
        args.file_from,
        args.file_to,
        args.format_from,
        args.format_to
    )

    format_mapping: dict[str, Any] = {
        'json': JSONSerializer(),
        'xml': XMLSerializer()
    }

    with open(file_from, 'r') as ff, open(file_to, 'w+') as ft:
        format_from = format_mapping[format_from]
        format_to = format_mapping[format_to]

        format_to.dump(format_from.load(ff), ft)


if __name__ == "__main__":
    main()
    