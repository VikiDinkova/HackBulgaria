def count_zero_neighbours(numbers):
	count = 0
	for index in range(len(numbers) - 1):
		if numbers[index] + numbers[index + 1] == 0:
			count += 1
	return count


numbers = [1, 2, -2, 0, 0, 5, -5]
print(count_zero_neighbours(numbers))
