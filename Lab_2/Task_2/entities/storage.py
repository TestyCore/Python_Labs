import pickle
import os
from re import match
from typing import NoReturn
import Lab_2.Task_2.helpers.file_manager as fm


class Storage:

    __FILE_PATH = os.path.relpath('data/')

    def __init__(self):
        self.__data = set()

    @property
    def data(self) -> set[str]:
        """Getter"""
        return self.__data

    @data.setter
    def data(self, new_data: set[str]) -> NoReturn:
        """Setter"""
        self.__data = new_data

    def add(self, keys: tuple[str]):
        """Adds new keys to the storage"""
        self.data.update(keys)

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
        """Checks if key exists"""

        if key in self.data:
            return True
        else:
            return False

    def grep(self, regex: str) -> list:
        """Regex to find elements in storage"""
        try:
            return list(filter(lambda k: match(regex, k), self.data))
        except os.error:
            return []

    def load(self, username: str, switch=False):
        """Loads data from file"""

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

        if switch:
            self.data = new_data
        else:
            self.data.update(new_data)

    def save(self, username: str):
        """Saves data to file"""

        path: str = fm.get_path(self.__FILE_PATH, f"{username}.pkl")

        with open(path, 'wb+') as file:
            pickle.dump(self.data, file)
