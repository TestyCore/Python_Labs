from .user import User


class Terminal:

    def __init__(self):
        self.__user: str = ""

    def start(self):
        print("E63 S")
        self.__user = "dodik"
        print(self.__user)
