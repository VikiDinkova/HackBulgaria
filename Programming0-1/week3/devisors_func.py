def devisors(number):
	devisors = []
	start = 1
	while  start < number:
		if number % start == 0:
			devisors += [start]
		start += 1
	return devisors

number = int(input('Enter number: '))
print(devisors(number))