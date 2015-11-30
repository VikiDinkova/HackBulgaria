import sys
from random import randint


def main():
    filename = sys.argv[1]
    n = sys.argv[2]
    n = int(n)
    data = open(filename, 'w')
    while n != 0:
        data.write(str(randint(1, 1000)) + " ")
        n -= 1
    data.close()


if __name__ == '__main__':
    main()
