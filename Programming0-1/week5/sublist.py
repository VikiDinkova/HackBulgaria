def sublist(list1, list2):
	j = 0
	for i in range(len(list1)):
		if list1[i] == list2[j]:
			j += 1
		else:
			j = 0
			if list1[i] == list2[j]:
				j += 1
		if j == len(list2):
			return True
	return False


list2 = [1, 2, 3]
list1 = [0, 0, 1, 2, 1, 2, 3, 5, 6]
print(sublist(list1, list2))
