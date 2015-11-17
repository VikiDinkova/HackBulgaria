
def sum_ints(numbers):
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

	
number = int(input('Enter number: '))
print(sum_ints(number ))