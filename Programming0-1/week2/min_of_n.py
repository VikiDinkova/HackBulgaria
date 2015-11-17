n = int(input('Enter n: '))
count = 0
list_ = []

while count < n:
	number = int(input(' '))
	list_ += [number]
	count += 1
list_.sort()
print('Min is {0}'.format(list_[0]))
