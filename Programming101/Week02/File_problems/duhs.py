import sys
import os


def main():
    path = sys.argv[1]
    if os.path.exists(path):
        print(os.path.getsize(path) / 512)


if __name__ == '__main__':
    main()
