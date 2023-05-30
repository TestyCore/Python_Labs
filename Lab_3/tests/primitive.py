import unittest

from serializers.jsonserializer import JSONSerializer
from serializers.xmlserializer import XMLSerializer


class PrimitiveTypes(unittest.TestCase):
    json = JSONSerializer()
    xml = XMLSerializer()

    def test_json_dumps(self):
        self.assertEqual(self.json.dumps("777"), '"777"')
        self.assertEqual(self.json.dumps(777), "777")
        self.assertEqual(self.json.dumps(777.0), "777.0")
        self.assertEqual(self.json.dumps(3j + 2), "(2+3j)")
        self.assertEqual(self.json.dumps("string"), '"string"')
        self.assertEqual(self.json.dumps(True), "true")
        self.assertEqual(self.json.dumps(None), "none")
        self.assertEqual(self.json.dumps(""), '""')

    def test_json_loads(self):
        self.assertEqual(self.json.loads('"777"'), "777")
        self.assertEqual(self.json.loads("777"), 777)
        self.assertEqual(self.json.loads("777.0"), 777.0)
        self.assertEqual(self.json.loads("(2+3j)"), 2 + 3j)
        self.assertEqual(self.json.loads("true"), True)
        self.assertEqual(self.json.loads("none"), None)
        self.assertEqual(self.json.loads('"True"'), "True")
        self.assertEqual(self.json.loads('""'), "")
        self.assertEqual(self.json.loads(""), None)

    def test_json_dumps_and_loads(self):
        self.assertEqual(self.json.loads(self.json.dumps("777")), "777")
        self.assertEqual(self.xml.loads(self.xml.dumps("777")), "777")

        self.assertEqual(self.json.loads(self.json.dumps(777)), 777)
        self.assertEqual(self.xml.loads(self.xml.dumps(777)), 777)

        self.assertEqual(self.json.loads(self.json.dumps(777.0)), 777.0)
        self.assertEqual(self.xml.loads(self.xml.dumps(777.0)), 777.0)

        self.assertEqual(self.json.loads(self.json.dumps(2 + 3j)), 2 + 3j)
        self.assertEqual(self.xml.loads(self.xml.dumps(2 + 3j)), 2 + 3j)

        self.assertEqual(self.json.loads(self.json.dumps("False")), "False")
        self.assertEqual(self.xml.loads(self.xml.dumps("True")), "True")

        self.assertEqual(self.json.loads(self.json.dumps(True)), True)
        self.assertEqual(self.xml.loads(self.xml.dumps(None)), None)

    def test_dump_and_load(self):
        with (open("from.txt", "w+") as f, open("from.txt", "r") as t):
            self.json.dump("777", f)
            f.seek(0)
            self.assertEqual(self.json.load(t), '777')

        with (open("from.txt", "w+") as f, open("from.txt", "r") as t):
            self.json.dump(777, f)
            f.seek(0)
            self.assertEqual(self.json.load(t), 777)

        with (open("from.txt", "w+") as f, open("from.txt", "r") as t):
            self.json.dump(777.7, f)
            f.seek(0)
            self.assertEqual(self.json.load(t), 777.7)

        with (open("from.txt", "w+") as f, open("from.txt", "r") as t):
            self.json.dump(2+3j, f)
            f.seek(0)
            self.assertEqual(self.json.load(t), 3j+2)

        with (open("from.txt", "w+") as f, open("from.txt", "r") as t):
            self.json.dump("string", f)
            f.seek(0)
            self.assertEqual(self.json.load(t), "string")

        with (open("from.txt", "w+") as f, open("from.txt", "r") as t):
            self.json.dump(True, f)
            f.seek(0)
            self.assertEqual(self.json.load(t), True)

        with (open("from.txt", "w+") as f, open("from.txt", "r") as t):
            self.json.dump("", f)
            f.seek(0)
            self.assertEqual(self.json.load(t), "")


if __name__ == '__main__':
    unittest.main()
