import Task_1.helpers.constants as constants
import re


def process_abbreviations(text: str) -> str:
    """Remove all dots in abbreviations"""

    for abbr in constants.ABBREVIATIONS:
        text = text.replace(abbr, abbr.replace('.', ''))

    return text


def replace_endings(text: str) -> str:
    """Replace '?' and '!' and '...' with period"""

    for word in text.split():

        if re.search(r'[!?]+[!?.]*[!?.]*|[!?.]+[!?.]+[!?.]*', word):
            text = text.replace(word, '.')

    return text


def remove_punctuation(text: str) -> str:
    """Remove punctuation signs except endings"""

    for sign in constants.PUNCTUATION:
        text = text.replace(sign, ' ')

    return text


def process_floats(text: str) -> str:
    """Removes periods in float numbers"""

    for word in text.split():
        try:
            float(word)
            text = text.replace(word, word.replace('.', ''))
        finally:
            continue

    return text


def process_extensions(text: str) -> str:
    """Remove period in file extensions"""

    for ext in constants.EXTENSIONS:
        text = text.replace(ext, '')

    return text


def process_dates(text: str) -> str:
    """Remove periods in dates"""

    for word in text.split():

        if re.search(r'\d{2}.\d{2}.\d{4}', word):
            text = text.replace(word, word.replace('.', ''))

    return text


def get_words(text: str) -> list[str]:
    """Returns list of all words in the text"""

    text = re.sub(r"[!?.,;:-]", '', text)
    words = list()

    for word in text.split():
        try:
            float(word)
        except ValueError:
            words.append(word)

    return words


def count_words(text: str) -> int:
    """Amount of words in text"""

    return len(get_words(text))


def count_characters(text: str) -> int:
    """Counts amount of all characters in words only"""

    words = get_words(text)

    if len(words) == 0:
        return 0

    characters = 0

    for word in words:
        characters += len(word)

    return characters
