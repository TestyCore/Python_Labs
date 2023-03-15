from Task_1.helpers.constants import ABBREVIATIONS, SENTENCE_ENDINGS


def omit_abbreviations(text: str) -> str:
    """Remove all dots in abbreviations"""

    for abbr in ABBREVIATIONS:
        text = text.replace(abbr, abbr.replace('.', ''))

    return text


def replace_endings(text: str) -> str:
    """Replace '?' and '!' and '...' with period"""

    for ending in SENTENCE_ENDINGS:
        text = text.replace(ending, '.')

    return text


def replace_floats(text: str) -> str:
    """Removes periods in float numbers"""

    text = text.replace(',', '')

    for word in text.split():
        try:
            float(word)
            text = text.replace(word, word.replace('.', ''))

        finally:
            continue

    return text


def count_sentences(text: str) -> int:
    """Amount of sentences in the text"""

    text = omit_abbreviations(text)
    text = replace_endings(text)
    text = replace_floats(text)

    if not text.endswith('.'):
        text = text + '.'

    return len(text.split('.')) - 1
