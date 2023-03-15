from utilities.input import get_text
from utilities.parse_text import omit_abbreviations, count_sentences


def main():
    print("Choose the way to get text:\n" +
          "1. Input manually\n" +
          "2. Specify the PATH to .txt file\n")

    text = get_text()

    print(text)
    print("\nAmount of sentences: " + count_sentences(text).__str__())


if __name__ == '__main__':
    main()
