n = int(input('Enter n: '))
count = 0
list_ = []

while count < n:
	number = int(input(' '))
	count += 1
	list_ += [number]

list_.sort()
print(list_[len(list_) - 1])
