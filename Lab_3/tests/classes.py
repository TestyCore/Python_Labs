import unittest

from serializers.jsonserializer import JSONSerializer


class User:
    common = 777

    def __init__(self, username: str):
        self.username = username

    def change(self):
        self.username = "Anton"
        return self.username

    @staticmethod
    def pri():
        return "Vorontsov"

    def __repr__(self):
        return f"User('{self.username}')"

    def __str__(self):
        return f"Username - {self.username}"

    @classmethod
    def get_common(cls):
        return cls.common


class Admin(User):
    admin = "admin"

    def __init__(self, bb):
        self.surname = "adminovich"

    @classmethod
    def get_name(cls):
        return cls.admin + "----" + cls.common.__str__()


class Test(unittest.TestCase):
    json = JSONSerializer()

    def test_1(self):
        self.assertEqual(
            self.json.loads(self.json.dumps(User("Slava"))).username,
            User("Slava").username
        )
        self.assertEqual(
            self.json.loads(self.json.dumps(User)).pri(),
            User.pri()
        )

    def test_2(self):
        self.assertEqual(
            self.json.loads(self.json.dumps(User("slava"))).__repr__(),
            User("slava").__repr__()
        )
        self.assertEqual(
            self.json.loads(self.json.dumps(User("slava"))).change(),
            User("slava").change()
        )
        self.assertEqual(
            self.json.loads(self.json.dumps(User("Slava"))).get_common(),
            User("Slava").get_common()
        )

    def test_3(self):
        self.assertEqual(
            self.json.loads(self.json.dumps(Admin("slava"))).get_name(),
            Admin("slava").get_name()
        )


if __name__ == '__main__':
    unittest.main()
