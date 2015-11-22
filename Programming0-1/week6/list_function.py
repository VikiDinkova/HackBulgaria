def head(arr):
	return arr[0]

print(head([1, 2, 3]))


def last(arr):
	return arr[len(arr) - 1]

print(last([1, 3, 55, 6, 3]))


def tail(arr):
	new_arr = []
	for index in range(1, len(arr)):
		new_arr.append(arr[index])
	return new_arr

print(tail([1, 3, 55, 6, 3]))

def equal_list(list1, list2):
	j  = 0
	for i in range(len(list1)):
		if list1[i] == list2[j]:
			j += 1
		else:
			j = 0
		if j == len(list2):
			return True
	return False

print(equal_list([1, 2], [1, 2, 3, 5]))


def count_item(arr, element):
	count = 0
	for el in arr:
		if el == element:
			count += 1
	return count


print(count_item([1, 3, 5, 6], 1))

def take(digit, arr):
	new_arr = []
	for i in range(len(arr)):
		if i <= digit and i < len(arr):
			new_arr.append(arr[i])
	return new_arr

print(take(4, [1, 2, 3, 4, 5, 6, 7]))


def drop(digit, arr):
	new_arr = []
	for i in range(len(arr)):
		if i != digit and i < len(arr):
			new_arr.append(arr[i])
		return new_arr

print(drop(1, [1, 2, 3]))

def reverse(arr):
	return arr[::-1]

print(reverse(["Speak", "in", "reverse", "you", "must!"]))
print(reverse([1, 2, 3]))
print(reverse([]))