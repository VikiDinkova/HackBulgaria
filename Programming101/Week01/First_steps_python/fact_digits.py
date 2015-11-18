def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact


def fact_digits(number):
    sum_of_digits = 0

    while number != 0:
        temp = number % 10
        sum_of_digits += factorial(temp)
        number = number // 10

    return sum_of_digits


print(factorial(1))
print(factorial(4))
print(factorial(5))
print(fact_digits(145))
