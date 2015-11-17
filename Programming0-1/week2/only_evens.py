n = int(input('Enter n: '))
count = 0
list_ = []
list_even = []
count_even = 0

while count < n:
	m = int(input(''))
	list_ += [m]
	count += 1
print(list_)

for number in list_:
	while number % 2 == 0:
		print(number)
		count_even += 1
		number += 1
		list_even += [number]
print('Count of evens: {0}'.format(count_even))
print(list_even)
print('Evens are:')
for numbers in list_even:
 	print('{0}'.format(numbers - 1 ))

