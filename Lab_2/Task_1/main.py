from utilities.input import get_text
from utilities.parse_text import count_sentences, count_non_declare


def main():
    print("Choose the way to get text:\n" +
          "1. Input manually\n" +
          "2. Specify the PATH to .txt file\n")

    text = get_text()

    print(text)

    print("\nAmount of sentences: " + count_sentences(text).__str__())
    print("\nAmount of non-declarative: " + count_non_declare(text).__str__())


if __name__ == '__main__':
    main()
