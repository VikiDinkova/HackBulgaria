number = int(input('Enter number: '))
devisors = []
start = 2

while  start < number:
	if number % start == 0:
		devisors += [start]
	start += 1
print(devisors)