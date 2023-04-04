import os


def get_path(dir_path: str, name: str) -> str:
    """Creates a path to user folder """

    return os.path.join(dir_path, name)


def verify_path(path: str) -> bool:
    """Checks if the given path exists"""

    return os.path.lexists(path)
