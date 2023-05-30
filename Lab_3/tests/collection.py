import unittest

from serializers.jsonserializer import JSONSerializer
from serializers.xmlserializer import XMLSerializer


class JSONDataStructuresCase(unittest.TestCase):
    json: JSONSerializer = JSONSerializer()
    xml: XMLSerializer = XMLSerializer()

    def test_empty(self):
        self.assertEqual(self.json.loads(self.json.dumps({})), {})
        self.assertEqual(self.xml.loads(self.xml.dumps({})), {})

        self.assertEqual(self.json.loads(self.json.dumps(())), ())
        self.assertEqual(self.xml.loads(self.xml.dumps(())), ())

        self.assertEqual(self.json.loads(self.json.dumps([])), [])
        self.assertEqual(self.xml.loads(self.xml.dumps([])), [])

        self.assertEqual(self.json.loads(self.json.dumps(set())), set())
        self.assertEqual(self.xml.loads(self.xml.dumps(set())), set())

    def test_single_value(self):
        self.assertEqual(self.json.loads(self.json.dumps({"777": 777})), {"777": 777})
        self.assertEqual(self.xml.loads(self.xml.dumps({"777": 777})), {"777": 777})

        self.assertEqual(self.json.loads(self.json.dumps(([1, 2, 777]))), ([1, 2, 777]))
        self.assertEqual(self.xml.loads(self.xml.dumps(([1, 2, 777]))), ([1, 2, 777]))

        self.assertEqual(self.json.loads(self.json.dumps([777])), [777])
        self.assertEqual(self.xml.loads(self.xml.dumps([777])), [777])

        self.assertEqual(self.json.loads(self.json.dumps({7, 777})), {7, 777})
        self.assertEqual(self.xml.loads(self.xml.dumps({7, 777})), {7, 777})

    def test_nested(self):
        test = {
            1: 2,
            3: [None, set(), "string"],
            5: {
                6: {1, 2, 3},
                8: {
                    9: True,
                   10: (5, 6)
                },
            }
        }
        self.assertEqual(self.json.loads(self.json.dumps(test)), test)
        self.assertEqual(self.xml.loads(self.xml.dumps(test)), test)


if __name__ == '__main__':
    unittest.main()