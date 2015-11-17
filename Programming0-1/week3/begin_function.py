def square(a):
	return a * a

# a = int(input('Enter number: '))
# print(square(a))

def factorial(a):
 	fact = 1
 	while a > 0:
 		fact  *= a
 		a -= 1
 	return fact
# a = int(input('Enter number: '))
# print(factorial(a))

def count_elements(array):
	count = 0
	for element in array:
		count += 1
	return count
# array = [1,23,6543,6,4]
# print(count_elements(array))

def member(element, array):
	for el in array:
		if element == el:
			return True
	return False
	# return element in array
# array = [1, 3, 45, 234, 45, 35]
# number = int(input('Enter number: '))
# print(member(number, array))

students = ["Rado", "Ivo", "Maria", "Nina"]
grades = [3, 4.5, 5.5, 6]

def grades_that_pass(students, grades, limit):
	names = []
	for x in range(len(students)):
		if grades[x] >= limit:
			names += [students[x]]
	return names

print(grades_that_pass(students, grades, 4))