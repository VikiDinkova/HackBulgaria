def count_zero_pairs(numbers):
	count = 0
	for i in range(len(numbers) - 1):
		for j in range(i + 1 , len(numbers)):
			if numbers[i] + numbers[j] == 0:
				count += 1
	return count

numbers = [0, 2, -2, 5, 10]
print(count_zero_pairs(numbers))