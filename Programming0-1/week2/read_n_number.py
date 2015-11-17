n = int(input('Enter n :'))
count = 1
list_ = []
sum_ = 0

while count <= n:
	number = (int(input('Enter number: ')))
	count += 1
	list_ += [number] 
for el in list_:
	sum_ += list_[el]
	el += 1
print(sum_)