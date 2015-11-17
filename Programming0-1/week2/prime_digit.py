number = int(input('Enter number: '))
list_digits = []
temp = number
start = 2

while temp > 0:
	last_digit = temp % 10
	list_digits += [last_digit]
	temp = temp // 10
print(list_digits)
for digit in list_digits:
	if digit == 3 or digit == 5 or digit == 7:
		print(digit)

