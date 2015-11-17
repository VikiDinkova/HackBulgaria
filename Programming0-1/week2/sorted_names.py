number_of_names = int(input('Enter a number of names: '))
list_of_names = []
while number_of_names > 0:
	current_name = input('')
	list_of_names += [current_name]
	number_of_names -= 1
list_of_names.sort()
for name in list_of_names:
	print(name)