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


def count_sentences(text: str) -> int:
    """Amount of sentences in the text"""

    text = process_abbreviations(text)
    text = remove_punctuation(text)
    text = process_floats(text)
    text = process_extensions(text)
    text = process_dates(text)
    text = replace_endings(text)

    if not text.endswith('.'):
        text = text + '.'

    return len(text.split('.')) - 1


def count_non_declare(text: str) -> int:
    """ Amount of non-declarative sentences"""

    count = 0

    for word in text.split():
        if re.search(r'\?*!+\.*|\?+!*\.*|\.*\?+!*|\.*\?*!+', word):
            count += 1

    return count


def count_words(text: str) -> int:
    """Amount of words in text"""

    text = re.sub(r"[!?.,;:-]", '', text)
    counter = 0

    for word in text.split():
        try:
            float(word)
        except ValueError:
            counter += 1

    return counter


def count_average_word_length(text: str) -> float:
    text = re.sub(r"[!?.,;:-]", '', text)
    characters = 0

    for word in text.split():
        try:
            float(word)
        except ValueError:
            characters += len(word)

    return characters / count_words(text)
