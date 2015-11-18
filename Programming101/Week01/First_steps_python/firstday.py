def sum_of_digits(digits):
	sum_ = 0

	while digits != 0:
		i = digits % 10
		sum_ += i
		digits = digits // 10
		print(digits)

	return sum_

#print(sum_of_digits(-4250))


def count_digit(n):
    return sum([1 for x in str(n)])


def to_number(digit_list):
    # digit = ''.join(digit_list)
    # return int(digit)

    number = 0
    power = len(digit_list) - 1

    for digit in digit_list:
        number += digit * (10 ** power)
        power -= 1

    return number


# print(to_number([1, 2, 4]))

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


# print(factorial(1))
# print(factorial(4))
# print(factorial(5))
# print(fact_digits(145))

def fibonacci(number):
    list_fib = [1, 1]

    for i in range(0, number - 2):
        next_digit = list_fib[i] + list_fib[i + 1]
        list_fib.append(next_digit)

    return list_fib

def fibonacci(n):
    result = []
    a = 1
    b = 1
    # a, b = 1, 1

    while len(result) < n:
        result.append(a)
        next_number = a + b
        a = b
        b = next_number
        # a, b = b, a + b 
        # bez mejdinna promenliva

    return result


def fibonacci_rec(number):
    if number == 1 or number == 2:
        return 1
    return(fibonacci_rec(number - 1) + fibonacci_rec(number - 2))


# print(fibonacci_rec(10))


def palindrome(obj):
    return str(obj) ==  str(obj)[::-1]:
    

# print(palindrome(121))
# print(palindrome("kapak"))
# print(palindrome("baba"))

def count_vowels(str_):
	count = 0
	vowels = 'aeiouyAEIOUY'


	for i in str_:
		if i in vowels:
			count += 1
			
	return count


# print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))

def count_consonants(str_):
	count = 0
	consonants = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWZ'


	for i in str_:
		if i in consonants:
			count += 1
			
	return count

# print(count_consonants("Theistareykjarbunga"))

def char_histogram(string_):
    dict_ = {}

    for item in string_:
        dict_[item] = string_.count(item)

    return(dict_)

# print(char_histogram("AAAAaaa!!!"))

