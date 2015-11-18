def sum_of_digits(digits):
	sum_ = 0

	while digits != 0:
		i = digits % 10
		sum_ += i
		digits = digits // 10
		print(digits)

	return sum_


print(sum_of_digits(-4250))