from entities.terminal import Terminal
from entities.storage import Storage
from helpers.arg_parser import arg_parse

from Lab_2.Task_2.entities.user import User


def main():
    user = User("denis")
    user.load_data()
    user.list_keys()

    args = arg_parse(input("˜ "))

    if len(args) != 0:
        user.add_keys(args)
    else:
        print("mda....")

    user.list_keys()

    args = input("find: ")
    user.remove_key(args)
    user.save_data()


if __name__ == '__main__':
    main()
