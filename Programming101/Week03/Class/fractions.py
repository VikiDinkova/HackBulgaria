class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self):
        pass

    def __sub__(self):
        pass

    def __mul__(self):
        pass

    def __eq__(self):
        pass


a = Fraction(1, 2)
b = Fraction(2, 4)

a == b  # True

a + b  # 1
a - b  # 0
a * b  # 1 / 4
