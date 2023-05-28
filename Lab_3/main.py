from serializers.jsonserializer import JSONSerializer


class User:

    def __init__(self, username: str):
        self.username = username

    def change(self):
        self.username = "anton"

    @classmethod
    def username(cls, a) -> str:
        """Getter"""

        return "self._username" * a


def main():
    a = User("slava")

    json = JSONSerializer()
    print(json.dumps(a))


if __name__ == "__main__":
    main()
    