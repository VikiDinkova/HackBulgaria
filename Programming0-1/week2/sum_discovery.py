number = int(input('Enter number: '))
devisors = []
start = 2
sum_devisors = 0

while  start < number:
	if number % start == 0:
		devisors += [start]
	start += 1
print(devisors)
print(sum(devisors))
for devisor in devisors:
	sum_devisors += devisor
print(sum_devisors)