import Lab_2.Task_1.helpers.constants as constants
import re


def process_abbreviations(text: str) -> str:
    """Remove all dots in abbreviations"""

    for abbr in constants.ABBREVIATIONS:
        text = text.replace(abbr, abbr.replace('.', ''))

    return text


def get_words(text: str) -> list[str]:
    """Returns list of all words in the text"""

    text = process_abbreviations(text)

    text = re.sub(r"[!?.,;:-]", '', text)
    text = re.sub(r"[!-/:-?@\[-_{-˜]", '', text)

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


def if_term_marks_only(text: str) -> bool:
    """ Checks if text contains only '?', '!', '.', ' ' """

    matches = re.search(r'([ .?!])+', text)

    if matches is None:
        return False

    if text == matches.group(0):
        return True
    else:
        return False

