from Lab_2.Task_2.helpers.constants.messages import CLI_COMMANDS


def arg_parse(prompt: str) -> tuple[str]:
    """ validates cli prompt and returns args"""

    comm_args = prompt.split(maxsplit=1)

    if len(comm_args) < 2:  # If now arguments provided
        return tuple()

    comm = comm_args[0]  # Get command

    if comm not in CLI_COMMANDS.keys():  # Check if such command exists
        print(f"Unknown command '{comm}.")
        return tuple()

    args_list = comm_args[1].split(',')  # Get list of arguments

    for arg in range(len(args_list)):  # Remove spaces around each argument
        args_list[arg] = args_list[arg].strip()

    args_list[:] = (value for value in args_list if value != "")

    return tuple(args_list)



