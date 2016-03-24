from decorators import accepts
from decorators import encrypt
from decorators import log
from decorators import performance
from time import sleep


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)


@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True


@encrypt(2)
def get_low_1():
    return "Get get get low"


@log('log.txt')
@encrypt(2)
def get_low():
    return "Get get get low"


@performance('log.txt')
def something_heavy():
    sleep(2)
    return "I am done!"


if __name__ == '__main__':
    print(say_hello("Viki"))
    print(deposit("RadoRado", 10))
    print(get_low_1())
    print(get_low())
    print(something_heavy())
