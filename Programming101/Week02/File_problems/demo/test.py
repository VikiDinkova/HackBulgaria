import sys


# def main():
#     res = 0
#     for argument in sys.argv[1:]:
#         res += int(argument)

#     return res


# if __name__ == '__main__':
#     print(main())

#open and read
# def main():
#     filename = sys.argv[1]
#     data = open(filename, 'r')

#     print(data.read())

#     data.close()

# if __name__ == '__main__':
#     main()

#write
def main():
    # filename = 'panda.txt'
    # data = open(filename, 'w')
    # data.write("Hello, I'm panda \n")

    # data.close()

    filename = 'panda.txt'
    with open(filename, 'w') as data:
        data.write("Hello, I'm panda \n")

if __name__ == '__main__':
    main()