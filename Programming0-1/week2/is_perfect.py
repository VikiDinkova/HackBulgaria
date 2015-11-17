number = int(input('Enter number: '))
devisors = []
start = 1
sum_devisors = 0
while  start < number:
	if number % start == 0:
		devisors += [start]
	start += 1
print(devisors)
for devisor in devisors:
	sum_devisors += devisor
print(sum_devisors)
if sum_devisors == number:
	print('The number is perfect')
else:
	print('The number is not perfect')

