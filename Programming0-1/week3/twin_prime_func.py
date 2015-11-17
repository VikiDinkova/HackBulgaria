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


number = int(input('Enter number: '))
if is_prime(number):
	before_prime_number = number - 2
	if is_prime(before_prime_number):
		print('Twin primes with {0}:\n{1}, {0}'.format(number, before_prime_number))

	after_prime_number = number + 2
	if is_prime(after_prime_number):
		print('{0}, {1}'.format(number, after_prime_number))	
	if not is_prime(before_prime_number) and not is_prime(after_prime_number):
		print("{0} is prime but:".format(number))
		print("{0} in not".format(before_prime_number))
		print("{0} in not".format(after_prime_number))
else:
    print('{0} is not prime'.format(number))
