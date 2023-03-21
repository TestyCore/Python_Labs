from Lab_2.Task_2.helpers.constants.messages import CLI_COMMANDS
import re

def command_parse(prompt: str) -> str:

    comm_args = prompt.split(maxsplit=1)

    if len(comm_args) == 0:
        return "Unknown command"

    comm = comm_args[0]

    if comm not in CLI_COMMANDS.keys():  # Check if such command exists
        return f"Unknown command '{comm}'."
    else:
        return comm


def arg_parse(prompt: str, isgrep: bool = False) -> tuple[str]:
    """ validates cli prompt and returns args"""

    comm_args = prompt.split(maxsplit=1)

    if len(comm_args) < 2:  # If now arguments provided
        return tuple()

    comm = comm_args[0]  # Get command

    if comm not in CLI_COMMANDS.keys():  # Check if such command exists
        print(f"Unknown command '{comm}.")
        return tuple()

    if isgrep:
        return tuple(comm_args[1])

    args_list = comm_args[1].split(',')  # Get list of arguments

    for arg in range(len(args_list)):  # Remove spaces around each argument
        args_list[arg] = args_list[arg].strip()

    args_list[:] = (value for value in args_list if value != "")

    return tuple(args_list)


def get_choice(prompt: str) -> str:

    while True:
        choice = input(prompt)

        if choice == 'y' or choice == 'n':
            return choice


def validate_username(name: str) -> bool:

    name = name.strip()
    match = re.match(r'(?<!\S)[A-Za-z]+(?!\S)', name)

    if match is not None and name == match.group(0):
        return True
    else:
        return False


def get_username() -> str:
    while True:
        name = input("Login as (username): ")

        if validate_username(name):
            return name
        else:
            print("Only latin letters!\n")




