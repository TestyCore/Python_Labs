import unittest
import Lab_2.Task_1.utilities.parser as prs


class TestCountSentences(unittest.TestCase):
    def test_zero_result(self):
        self.assertEqual(prs.count_sentences("123!", False), 0)
        self.assertEqual(prs.count_sentences("", False), 0)
        self.assertEqual(prs.count_sentences("!", False), 0)
        self.assertEqual(prs.count_sentences("?", False), 0)
        self.assertEqual(prs.count_sentences(".", False), 0)
        self.assertEqual(prs.count_sentences("...", False), 0)
        self.assertEqual(prs.count_sentences("!?!??!?!? .. !? ! ? ? ... !?", False), 0)

    def test_one_sentence(self):
        self.assertEqual(prs.count_sentences("a.", False), 1)
        self.assertEqual(prs.count_sentences("Hello Mr. Slava at 8 p.m....?", False), 1)
        self.assertEqual(prs.count_sentences(
            "Something long with [sa''d[as]d3593 '4wto3'g.", False), 1)

    def test_two_sentences(self):
        self.assertEqual(prs.count_sentences("hi!!?..?? ok", False), 2)


class TestCountNonDeclarative(unittest.TestCase):
    def test_zero_non_declarative(self):
        self.assertEqual(prs.count_sentences("", True), 0)
        self.assertEqual(prs.count_sentences(".", True), 0)
        self.assertEqual(prs.count_sentences("...", True), 0)
        self.assertEqual(prs.count_sentences("?", True), 0)
        self.assertEqual(prs.count_sentences("!", True), 0)
        self.assertEqual(prs.count_sentences("!??!? .. ! ???!", True), 0)

    def test_one_non_declarative(self):
        self.assertEqual(prs.count_sentences("text..!?!?!", True), 1)
        self.assertEqual(prs.count_sentences("Hello mr. Slava at 8 p.m....!?", True), 1)

    def test_many_non_declarative_many_signs(self):
        self.assertEqual(prs.count_sentences("a...!?? a b!? c..!", True), 3)


class TestAverageWordLength(unittest.TestCase):
    def test_zero_result(self):
        self.assertEqual(prs.count_avg_word_length("  .. . .. !?? !? ? !? ?! "), 0)
        self.assertEqual(prs.count_avg_word_length(""), 0)

    def test_one_letter(self):
        self.assertEqual(prs.count_avg_word_length("A"), 1)

    def test_one_word_many_letters(self):
        self.assertEqual(prs.count_avg_word_length(
            "COOLBUGSFACTONEDAYYOUWILLANSWERFORYO- -URACTIONS"), 22.5)

    def test_many_words_many_letters(self):
        self.assertEqual(prs.count_avg_word_length("abba sus 124912 imp0ster"), 5)


class TestAverageSentenceLength(unittest.TestCase):
    def test_zero_result(self):
        self.assertEqual(prs.count_avg_sentence_length(""), 0)
        self.assertEqual(prs.count_avg_sentence_length(
            "  .. . . . .. !?? !?? ? !? ! ?! "), 0)

    def test_one_char_long(self):
        self.assertEqual(prs.count_avg_sentence_length("a...!??!!??!?!"), 1)
        self.assertEqual(prs.count_avg_sentence_length(".?.?.?!  A.!"), 1)

    def test_two_sentences_many_words(self):
        self.assertEqual(prs.count_avg_sentence_length(
            """COOL BUGS 98123749812374 FACT: ONE DAY 14 YOU 
            WILL. 0 ANSWER ___FOR YOUR ACTIONS."""), 22.5)

    def test_many_sentences_many_words(self):
        self.assertAlmostEqual(prs.count_avg_sentence_length(
            "a b. c? abba!! ab, ba.. bobA AA..? .! . ?. sjf> as."), 3.67)


class TestTopKNGrams(unittest.TestCase):
    def test_zero_result(self):
        self.assertEqual(prs.top_k_n_grams('. - 123 123 123 123 234 234 6 !!'), [])
        self.assertEqual(prs.top_k_n_grams('akjsdnkjansdkjnasdkjn'), [])

    def test_one_n_gram(self):
        self.assertEqual(prs.top_k_n_grams('a b c d'), ['a b c d'])

    def test_four_n_grams(self):
        self.assertEqual(
            prs.top_k_n_grams('a b c d a b c d')[0],
            'a b c d'
        )
