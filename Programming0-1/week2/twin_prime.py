from math import sqrt

number = int(input('Enter number: '))
sq_root_number = sqrt(number)
is_prime = True
if number == 1:
	is_prime = False
start = 2

while start <= sq_root_number:
    if number % start == 0:
        is_prime = False
        break
    start += 1
if is_prime:
	before_prime_number = number - 2
	sq_root_other_number = sqrt(before_prime_number)
	before_number_is_prime = True
	if before_prime_number == 1:
		before_number_is_prime = False
	start_before_prime_number = 2
	while start_before_prime_number <= sq_root_other_number:
		if before_prime_number % start_before_prime_number == 0:
			before_number_is_prime = False
		start_before_prime_number += 1
	if before_number_is_prime:
		print('Twin primes with {0}:\n{1}, {0}'.format(number, before_prime_number))

	after_prime_number = number + 2
	sq_root_other_number = sqrt(after_prime_number)
	after_number_is_prime = True
	if after_prime_number == 1:
		after_number_is_prime = False
	start_after_prime_number = 2
	while start_after_prime_number <= sq_root_other_number:
		if after_prime_number % start_after_prime_number == 0:
			after_number_is_prime = False
		start_after_prime_number += 1
	if after_number_is_prime:
		print('{0}, {1}'.format(number, after_prime_number))	
	if before_number_is_prime == False and after_number_is_prime == False:
		print("{0} is prime but:".format(number))
		print("{0} in not".format(before_prime_number))
		print("{0} in not".format(after_prime_number))
else:
    print('{0} is not prime'.format(number))
