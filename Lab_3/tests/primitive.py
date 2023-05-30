import unittest

from serializers.jsonserializer import JSONSerializer
from serializers.xmlserializer import XMLSerializer


class PrimitiveTypes(unittest.TestCase):
    json_ser = JSONSerializer()
    xml_ser = XMLSerializer()

    def test_json_dumps(self):
        self.assertEqual(self.json_ser.dumps("777"), '"777"')
        self.assertEqual(self.json_ser.dumps(777), "777")
        self.assertEqual(self.json_ser.dumps(777.0), "777.0")
        self.assertEqual(self.json_ser.dumps(3j + 2), "(2+3j)")
        self.assertEqual(self.json_ser.dumps("string"), '"string"')
        self.assertEqual(self.json_ser.dumps(True), "true")
        self.assertEqual(self.json_ser.dumps(None), "none")
        self.assertEqual(self.json_ser.dumps(""), '""')

    def test_json_loads(self):
        self.assertEqual(self.json_ser.loads('"777"'), "777")
        self.assertEqual(self.json_ser.loads("777"), 777)
        self.assertEqual(self.json_ser.loads("777.0"), 777.0)
        self.assertEqual(self.json_ser.loads("(2+3j)"), 2 + 3j)
        self.assertEqual(self.json_ser.loads("true"), True)
        self.assertEqual(self.json_ser.loads("none"), None)
        self.assertEqual(self.json_ser.loads('"True"'), "True")
        self.assertEqual(self.json_ser.loads('""'), "")
        self.assertEqual(self.json_ser.loads(""), None)

    def test_json_dumps_and_loads(self):
        self.assertEqual(self.json_ser.loads(self.json_ser.dumps("777")), "777")
        self.assertEqual(self.xml_ser.loads(self.xml_ser.dumps("777")), "777")

        self.assertEqual(self.json_ser.loads(self.json_ser.dumps(777)), 777)
        self.assertEqual(self.xml_ser.loads(self.xml_ser.dumps(777)), 777)

        self.assertEqual(self.json_ser.loads(self.json_ser.dumps(777.0)), 777.0)
        self.assertEqual(self.xml_ser.loads(self.xml_ser.dumps(777.0)), 777.0)

        self.assertEqual(self.json_ser.loads(self.json_ser.dumps(2 + 3j)), 2 + 3j)
        self.assertEqual(self.xml_ser.loads(self.xml_ser.dumps(2 + 3j)), 2 + 3j)

        self.assertEqual(self.json_ser.loads(self.json_ser.dumps("False")), "False")
        self.assertEqual(self.xml_ser.loads(self.xml_ser.dumps("True")), "True")

        self.assertEqual(self.json_ser.loads(self.json_ser.dumps(True)), True)
        self.assertEqual(self.xml_ser.loads(self.xml_ser.dumps(None)), None)

    # def test_dump_and_load(self):
    #     with (
    #         open(os.path.join(DATA_DIR, "dump_and_load.json"), "w+") as fw,
    #         open(os.path.join(DATA_DIR, "dump_and_load.json"), "r") as fr
    #     ):
    #         self.json_ser.dump("14", fw)
    #         fw.seek(0)
    #         self.assertEqual(self.json_ser.load(fr), '14')
    #
    #     with (
    #         open(os.path.join(DATA_DIR, "dump_and_load.json"), "w+") as fw,
    #         open(os.path.join(DATA_DIR, "dump_and_load.json"), "r") as fr
    #     ):
    #         self.json_ser.dump(14, fw)
    #         fw.seek(0)
    #         self.assertEqual(self.json_ser.load(fr), 14)
    #
    #     with (
    #         open(os.path.join(DATA_DIR, "dump_and_load.json"), "w+") as fw,
    #         open(os.path.join(DATA_DIR, "dump_and_load.json"), "r") as fr
    #     ):
    #         self.json_ser.dump(14.0, fw)
    #         fw.seek(0)
    #         self.assertEqual(self.json_ser.load(fr), 14.0)
    #
    #     with (
    #         open(os.path.join(DATA_DIR, "dump_and_load.json"), "w+") as fw,
    #         open(os.path.join(DATA_DIR, "dump_and_load.json"), "r") as fr
    #     ):
    #         self.json_ser.dump(0.9j + 14, fw)
    #         fw.seek(0)
    #         self.assertEqual(self.json_ser.load(fr), 0.9j + 14)
    #
    #     with (
    #         open(os.path.join(DATA_DIR, "dump_and_load.json"), "w+") as fw,
    #         open(os.path.join(DATA_DIR, "dump_and_load.json"), "r") as fr
    #     ):
    #         self.json_ser.dump("False", fw)
    #         fw.seek(0)
    #         self.assertEqual(self.json_ser.load(fr), "False")
    #
    #     with (
    #         open(os.path.join(DATA_DIR, "dump_and_load.json"), "w+") as fw,
    #         open(os.path.join(DATA_DIR, "dump_and_load.json"), "r") as fr
    #     ):
    #         self.json_ser.dump(False, fw)
    #         fw.seek(0)
    #         self.assertEqual(self.json_ser.load(fr), False)


if __name__ == '__main__':
    unittest.main()
