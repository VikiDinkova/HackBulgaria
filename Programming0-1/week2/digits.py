number = int(input('Enter number: '))
number_digits = []
number_again = 0

while number > 0:
	digit = number % 10
	number_digits += [digit]
	number = number // 10
number_digits = number_digits[::-1]
print(number_digits)
for digit in number_digits:
	number_again = number_again * 10 + digit
print(number_again)
