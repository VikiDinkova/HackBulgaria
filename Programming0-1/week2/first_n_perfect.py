number = int(input('Enter number of perfect numbers: '))

start_number = 1 
found_numbers = 0
while found_numbers != number:
	devisors = []
	start = 1
	sum_devisors = 0

	while start < start_number:
		if start_number % start == 0:
			devisors += [start]
		start += 1
	
	# for devisor in devisors:
	# 	sum_devisors += devisor

	if sum(devisors) == start_number:
		print(start_number)
		found_numbers += 1
	start_number += 1

