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

    # def __str__(self):
    #     return f"Username - {self.username}"


def main():
    a = User("slava")
    # print(a.__str__())
    # print(repr(a))


    # a = [1, 2, 5]
    json = JSONSerializer()
    b = json.dumps(a)
    c = json.loads(b)

    # c.change()
    print(c)
    # c.pri()


    # xml = XMLSerializer()
    # b = xml.dumps(a)
    # c = xml.loads(b)
    #
    # c.change()
    # print(c.username)
    # c.pri()


if __name__ == "__main__":
    main()
    