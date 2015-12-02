def LCM(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        lcm = LCM(self.denominator, other.denominator)
        num = (lcm // self.denominator * self.numerator) + (lcm // other.denominator * other.numerator)
        return '{}/{}'.format(num, lcm)

    def __sub__(self, other):
        lcm = LCM(self.denominator, other.denominator)
        num = (lcm // self.denominator * self.numerator) - (lcm // other.denominator * other.numerator)
        return '{}/{}'.format(num, lcm)

    def __mul__(self, other):
        return '{}/{}'.format(str(self.numerator * other.numerator), str(self.denominator * other.denominator))

    def __eq__(self, other):
        lcm = LCM(self.denominator, other.denominator)
        return (lcm // self.denominator * self.numerator) == (lcm // other.denominator * other.numerator)


a = Fraction(1, 2)
b = Fraction(2, 4)

print(a == b)  # True
print(a + b)  # 1
print(a - b)  # 0
print(a * b)  # 1 / 4
