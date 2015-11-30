import sys


def main():
    filename = sys.argv[1]
    sum_ = 0
    data = open(filename, 'r')
    numbers = data.read()
    numbers = numbers.split(' ')
    for digit in numbers:
        if digit.isdigit():
            sum_ += int(digit)
    data.close()

    return sum_


if __name__ == '__main__':
    print(main())
