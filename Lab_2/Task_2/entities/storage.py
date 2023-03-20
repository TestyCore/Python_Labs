import pickle
import os
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
            print(f"Aborting. No '{key}' matches found.")

    def list(self) -> list:
        """Returns list of elements"""

        return list(self.data)

    def find(self, key: str) -> str:
        """Returns key if key is present in __data"""

        if key in self.data:
            return key
        else:
            return "No '{key}' matches found."

    def load(self, username: str):
        """Loads data from storage container"""

        path: str = fm.get_path(self.__FILE_PATH, f"{username}.pkl")

        if not fm.verify_path(path):
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
