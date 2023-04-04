import Lab_2.Task_1.helpers.parse_helpers as prs
import re


def count_sentences(text: str, is_non_declare: bool) -> int:
    """Amount of sentences in the text"""

    if len(text) == 0 or prs.count_words(text) == 0 or prs.if_term_marks_only(text):
        return 0

    text = prs.process_abbreviations(text)
    text += '.'

    if is_non_declare:
        declare = re.findall(r'(?<=\w| )+([.])+(?= |$)', text)
        totally = re.findall(r'(?<=\w)+([?!.])+(?= |$)', text)

        if len(totally) - len(declare) < 0:
            return 0
        else:
            return len(totally) - len(declare)

    else:
        totally = re.findall(r'(?<=\w)+([?!.])+(?= |$)', text)

        return len(totally)


def count_avg_sentence_length(text: str) -> float:
    """Counts average sentence-length in the text"""

    if count_sentences(text, False) == 0:
        return 0

    return round(prs.count_characters(text) / (count_sentences(text, False)), 2)


def count_avg_word_length(text: str) -> float:
    """Counts average word-length in the text"""

    if len(prs.get_words(text)) == 0:
        return 0

    return round(prs.count_characters(text) / len(prs.get_words(text)), 2)


def top_k_n_grams(text: str, k: int = 10, n: int = 4) -> list[str]:
    """Returns top-K repeated N-grams in the text"""

    text = re.sub(r"[!?.,;:-]", '', text)

    words = prs.get_words(text)

    n_grams = list()

    for i in range(len(words)):

        if i + n <= len(words):
            n_grams.append(" ".join(words[i:i + n]))

    unique_n_grams = sorted(set(n_grams), key=n_grams.count, reverse=True)

    return unique_n_grams[:k]
