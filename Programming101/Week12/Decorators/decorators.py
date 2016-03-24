from datetime import datetime


def get_promotion(promotion_months):
    def accepter(func):
        def decorated(months, user_id):
            if months >= promotion_months:
                months += 1
            return func(months, user_id)
        return decorated
    return accepter


def accepts(*type_name):
    def accept(func):
        def decorated_func(*type_):
            if len(type_name) == len(type_):
                for i in range(0, len(type_name)):
                    if type(type_[i]) == type_name[i]:
                        return func(*type_)
                    return TypeError
            return TypeError
        return decorated_func
    return accept


def encrypt(moves):
    def decor(func):
        def decorated():
            new = ''
            for el in func():
                new += chr(ord(el) + moves)
            return new
        return decorated
    return decor


def log(file):
    def decor(func):
        def decorated():
            return "{} was created at {}".format(func.__name__, datetime.now())
        return decorated
    return decor


def performance(file_name):
    def decor(func):
        def decorated():
            return "{} was called and took {} seconds to complete".format(func.__name__, )
        return decorated
    return decor
