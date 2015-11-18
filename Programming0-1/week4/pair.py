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


def prime_pair(numbers):
	for i in range(len(numbers)):
		for j in range(i, len(numbers)):
			sum_ = numbers[i] + numbers[j]
			if is_prime(sum_):
				return True
	return False
	
numbers = [6, 6]
print(prime_pair(numbers))			



