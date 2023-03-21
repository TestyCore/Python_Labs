from __future__ import annotations

from Lab_2.Task_2.entities.storage import Storage
from Lab_2.Task_2.helpers.constants.messages import LOAD_QUESTION
from Lab_2.Task_2.helpers.input_manager import get_choice
from re import Pattern


class User:

    def __init__(self, username: str):
        self._username = username
        self._container = Storage()

    @property
    def username(self) -> str:
        """Getter of attribute _username"""

        return self._username

    @username.setter
    def username(self, new_username: str):
        """Setter of attribute __username"""

        self._username = new_username

    @property
    def container(self) -> Storage:
        """Getter of attribute __container"""

        return self._container

    def add_keys(self, *keys: tuple[str]):
        """Adds keys to container"""

        self.container.add(*keys)

    def remove_key(self, key: str):
        """Removes a single key from container"""

        self.container.remove(key)

    def list_keys(self):
        """Prints data in user-friendly format."""
        print(f"[{', '.join(self.container.list())}]")

    def find_keys(self, keys: tuple[str]):
        """Prints the output of Storage's find method"""
        matches = list()

        for key in keys:
            if self.container.find(key):
                matches.append(key)

        if len(matches) != 0:
            print(matches)
        else:
            print("No matches found.")

    def grep_keys(self, regex: str | bytes | Pattern[bytes]):
        """Prints the output of Storage's find method.

        :param regex: single regex tuple."""
        print(self.container.grep(regex))

    def save_data(self):
        """Saves data to the file with user's name as a filename."""
        self.container.save(self.username)

    def load_data(self):
        """Loads data from the file with user's name as a filename."""
        self.container.load(self.username)

    def switch(self, new_user: str):
        """Switches to another user"""
        
        ans: str = get_choice(LOAD_QUESTION.format(new_user))

        if ans == 'y':
            self._container.load(new_user, switch=True)
        elif ans == 'n':
            self.container.data = set()

        self.username = new_user


















