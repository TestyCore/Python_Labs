import sys
sys.path.append("../..")

from entities.terminal import Terminal


def main():
    term = Terminal()
    term.start()


if __name__ == '__main__':
    main()
