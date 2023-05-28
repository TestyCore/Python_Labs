from serializers.jsonserializer import JSONSerializer


class User:

    def __init__(self, username: str):
        self.username = username

    def change(self):
        self.username = "Anton"

    def pri(self):
        print("Vorontsov")

    @classmethod
    def username(cls, a) -> str:
        return "self._username" * a


def main():
    a = User("slava")
    json = JSONSerializer()
    b = json.dumps(a)
    c = json.loads(b)

    c.change()
    print(c.username)
    c.pri()


if __name__ == "__main__":
    main()
    