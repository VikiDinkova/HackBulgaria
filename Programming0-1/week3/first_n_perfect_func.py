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


def first_n_perfect(number_count):
	list_of_perfects = []
	current_number = 1
	while len(list_of_perfects) != number_count:
		if is_perfect(current_number):
			list_of_perfects += [current_number]
		current_number += 1
	return list_of_perfects


def print_list(input_list):
	for item in input_list:
		print(item)


number = int(input('Enter number of perfect numbers: '))
perfect_numbers = first_n_perfect(number)
print_list(perfect_numbers)
