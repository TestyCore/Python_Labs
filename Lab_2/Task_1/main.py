from utilities.process_input import get_selection


def main():
    print("Choose the way to get text:\n" +
          "1. Input manually\n" +
          "2. Specify the PATH to .txt file\n")

    selection = get_selection()


if __name__ == '__main__':
    main()

