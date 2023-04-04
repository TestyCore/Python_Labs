import sys
sys.path.append("../..")

from utilities.input import get_text, get_k_n
import utilities.parser as pars


def main():

    print("Choose the way to get text:\n" +
          "1. Input manually\n" +
          "2. Specify the PATH to .txt file\n")
    text = get_text()

    print("\nChoose the way to set K and N:\n" +
          "1. Input manually\n" +
          "2. Use default: K = 10, N = 4\n")
    k, n = get_k_n()

    print("\nText:\n" + text)
    print("\nAmount of sentences: " + pars.count_sentences(text, False).__str__())
    print("Amount of non-declarative: " + pars.count_sentences(text, True).__str__())
    print("Average sentence-length: " + pars.count_avg_sentence_length(text).__str__())
    print("Average word-length: " + pars.count_avg_word_length(text).__str__())
    print("Top-K repeated N-grams: " + pars.top_k_n_grams(text, k, n).__str__())


if __name__ == '__main__':
    main()
