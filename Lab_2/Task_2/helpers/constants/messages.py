CLI_COMMANDS: dict[str, str] = {
    "add": "- add one or more elements to the container ",
    "remove": "– delete element from container",
    "find": "- find certain element in container",
    "list": "– print all elements of container",
    "grep": "- find value in the container by regular expression",
    "save": "– save container to file",
    "load": "- load container from file",
    "switch": "- switches to another user",
    "whoami": "- shows current user"
}

START_MESSAGE: str = "\n*********** Commands ***********\n\n"

for comm in CLI_COMMANDS.keys():
    START_MESSAGE += f"{comm} {CLI_COMMANDS[comm]}\n"

LOAD_QUESTION: str = "Would you like to load '{}`s' data? [y/n]: "
SAVE_QUESTION: str = "Would you like to save '{}`s' data before switching? [y/n]: "
