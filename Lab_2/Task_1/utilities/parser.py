import Task_1.helpers.parse_helpers as prs
import re


def count_sentences(text: str) -> int:
    """Amount of sentences in the text"""

    text = prs.process_abbreviations(text)
    text = prs.remove_punctuation(text)
    text = prs.process_floats(text)
    text = prs.process_extensions(text)
    text = prs.process_dates(text)
    text = prs.replace_endings(text)

    if not text.endswith('.') and prs.count_words(text) != 0:
        text = text + '.'

    return len(text.split('.')) - 1


def count_non_declare(text: str) -> int:
    """ Amount of non-declarative sentences"""

    counter = 0

    for word in text.split():
        if re.search(r'\?*!+\.*|\?+!*\.*|\.*\?+!*|\.*\?*!+', word):
            counter += 1

    return counter


def count_avg_sentence_length(text: str) -> float:
    """Counts average sentence-length in the text"""

    return prs.count_characters(text) / (count_sentences(text))


def count_avg_word_length(text: str) -> float:
    """Counts average word-length in the text"""

    return prs.count_characters(text) / len(prs.get_words(text))


def top_k_n_grams(text: str, k: int = 10, n: int = 4) -> list[str]:
    """Returns top-K repeated N-grams in the text"""

    text = re.sub(r"[!?.,;:-]", '', text)

    words = prs.get_words(text)
    n_grams = tuple(
        " ".join(words[i:i+n])
        for i in range(len(words)) if i + n <= len(words)
    )

    unique_n_grams = sorted(set(n_grams), key=n_grams.count, reverse=True)

    return unique_n_grams[:k]
