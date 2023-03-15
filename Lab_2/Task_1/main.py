from utilities.input import get_input_way, get_text


def main():
    print("Choose the way to get text:\n" +
          "1. Input manually\n" +
          "2. Specify the PATH to .txt file\n")

    text = get_text()

    #print(text)


if __name__ == '__main__':
    main()

