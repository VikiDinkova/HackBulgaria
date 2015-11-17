n = int(input('Enter n : '))
count = 0
list_ = []

while count < n:
	number = int(input(' '))
	count += 1
	list_ += [number]
print('Avg is: {0}'.format(sum(list_) / n))

