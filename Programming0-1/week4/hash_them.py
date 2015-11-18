keys = ['one', 'two', 'three', 'four']
values = [1, 2, 3]
dictionary = {}


for index in range(len(keys)):
	if index < len(values):
		dictionary[keys[index]] = values[index]
	else:
		dictionary[keys[index]] = None

print(dictionary)