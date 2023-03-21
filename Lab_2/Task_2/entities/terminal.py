from __future__ import annotations

from Lab_2.Task_2.entities.user import User
from Lab_2.Task_2.helpers.input_manager import command_parse,\
                                               arg_parse,\
                                               validate_username,\
                                               get_username
from Lab_2.Task_2.helpers.constants.messages import START_MESSAGE, CLI_COMMANDS


class Terminal:

    def __init__(self):
        self.__prompt: str | None = None
        self.__user: User | None = None

        print(START_MESSAGE)

    def start(self):

        self.__user = User(get_username())

        while True:
            try:
                self.__prompt = input(f"{self.__user.username}: ")
                comm = command_parse(self.__prompt)

                if comm == "add":
                    self.add_command()
                elif comm == "remove":
                    self.remove_command()
                elif comm == "find":
                    self.find_command()
                elif comm == "list":
                    self.list_command()
                elif comm == "grep":
                    self.grep_command()
                elif comm == "save":
                    self.save_command()
                elif comm == "load":
                    self.load_command()
                elif comm == "switch":
                    self.switch_command()
                elif comm == "whoami":
                    self.whoami_command()
                else:
                    print(comm)
            except KeyboardInterrupt:
                print("STOOOOOP")

    def add_command(self):
        args = arg_parse(self.__prompt)

        if len(args) != 0:
            self.__user.add_keys(args)
        else:
            print("No arguments provided.")

    def remove_command(self):
        args = arg_parse(self.__prompt)

        if len(args) == 1:
            self.__user.remove_key(args[0])
        elif len(args) == 0:
            print("No arguments provided.")
        else:
            print("One argument expected")

    def find_command(self):
        args = arg_parse(self.__prompt)

        if len(args) != 0:
            self.__user.find_keys(args)
        else:
            print("No matches found.")

    def list_command(self):

        self.__user.list_keys()

    def grep_command(self):
        args = arg_parse(self.__prompt, True)

        if len(args) != 0:
            self.__user.grep_keys(''.join(args))
        else:
            print("No matches found.")

    def save_command(self):

        self.__user.save_data()

    def load_command(self):

        self.__user.load_data()

    def switch_command(self):
        args = arg_parse(self.__prompt)
        username = ''.join(args)

        if len(args) == 1 and validate_username(username):
            self.__user.switch(username)
        else:
            print("Invalid username.")

    def whoami_command(self):
        print(self.__user.username)






