def sum_ints(number):
	devisors = []
	start = 1
	sum_devisors = 0
	while  start < number:
		if number % start == 0:
			devisors += [start]
		start += 1
	for devisor in devisors:
		sum_devisors += devisor
	return sum_devisors


def is_perfect(number):
	return sum_ints(number) == number


number = int(input('Enter number: '))
print(is_perfect(number))