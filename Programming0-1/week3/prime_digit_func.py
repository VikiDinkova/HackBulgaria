from math import sqrt


def is_prime(number):
	current_dev = 2
	if number < 2:
		return False
	while current_dev <= sqrt(number):
		if number % current_dev == 0:
			return False
		current_dev += 1
	return True


def to_digits(number):
	list_of_digits = []
	while number != 0:
		last_digit = number % 10
		list_of_digits += [last_digit]
		number = number // 10
	return list_of_digits


def main():
	number = int(input('Enter number: '))
	list_of_digits = to_digits(number)
	for digit in list_of_digits:
		if is_prime(digit):
			print(digit)

if __name__ == '__main__':
	main()
