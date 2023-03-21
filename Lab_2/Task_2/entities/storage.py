from __future__ import annotations

import pickle
import os
from re import Pattern, match, error
from typing import NoReturn
import Lab_2.Task_2.helpers.file_manager as fm


class Storage:

    __FILE_PATH = os.path.relpath('data/')

    def __init__(self):
        self.__data = set()

    @property
    def data(self) -> set[str]:
        """Getter __date"""

        return self.__data

    @data.setter
    def data(self, new_data: set[str]) -> NoReturn:
        """Setter __data"""

        self.__data = new_data

    def add(self, *keys: tuple[str]):
        """Adds new keys to the storage"""

        self.data.update(*keys)

    def remove(self, key: str):
        """Removes key from storage"""

        if key in self.data:
            self.data.remove(key)
        else:
            print(f"No '{key}' matches found.")

    def list(self) -> list:
        """Returns list of elements"""

        return list(self.data)

    def find(self, key: str) -> bool:
        """Returns key if key is present in __data"""

        if key in self.data:
            return True
        else:
            return False

    def grep(self, regex: str | bytes | Pattern[bytes]) -> list:
        """Uses regular expressions to find elements in storage

        :param regex: regex-like object to filter data."""
        try:
            return list(filter(lambda k: match(regex, k), self.data))
        except os.error:
            return []

    def load(self, username: str, switch=False):
        """Loads data to storage from container with the given path.

        :param username : name of the source file to load data from;
        :param switch: if loading is performed on user switch or not."""
        path: str = fm.get_path(self.__FILE_PATH, f"{username}.pkl")

        if not fm.verify_path(path):
            if switch:
                self.data = set()
            return

        with open(path, 'rb') as file:
            try:
                new_data: set = pickle.load(file)
            except pickle.UnpicklingError:
                new_data = set()

        self.data = new_data

    def save(self, username: str):
        """Saves data to the file"""

        path: str = fm.get_path(self.__FILE_PATH, f"{username}.pkl")

        with open(path, 'wb+') as file:
            pickle.dump(self.data, file)
