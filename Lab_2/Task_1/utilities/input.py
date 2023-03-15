from os.path import exists as file_exists


def get_input_way() -> str:
    """ Returns choice how to get text (manually or from file) """

    while True:
        input_way = input("Choose [12]: ")

        if input_way == '1' or input_way == '2':
            return input_way


def get_text() -> str:
    """ Returns text according to chosen input_way """

    input_way = get_input_way()

    if input_way == '1':
        text = input('\nType text: ')
    else:
        text = load_file(input('\nPATH: '))

    return text


def process_path(file_path: str) -> str:
    """Ensures that .txt file exists in 'file_path' """

    file_path = file_path.strip()

    while True:
        if file_exists(file_path) and file_path.endswith('.txt'):
            return file_path
        else:
            print('Invalid PATH, or file does not exists!')
            file_path = input('\nPATH: ')


def load_file(file_path: str) -> str:
    """Returns text from specified .txt file"""

    file_path = process_path(file_path)

    with open(file_path, 'r', encoding='utf8') as file:
        return file.read()
