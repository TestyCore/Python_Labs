from Lab_2.Task_2.entities.storage import Storage


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

    def save_data(self):
        """Saves data to the file with user's name as a filename."""
        self.container.save(self.username)

    def load_data(self):
        """Loads data from the file with user's name as a filename."""
        self.container.load(self.username)

