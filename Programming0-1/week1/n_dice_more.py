from random import randint
number = int(input('Enter a number: '))
number = randint(1, number)
print('First roll %s' % number)
number_1 = int(input('Enter a number: '))
number_1 = randint(1, number_1)
print('Second roll: %s' % number_1)
number_2 = int(input('Enter a number: '))
number_2 = randint(1, number_2)
print('Third roll %s' % number_2)
sum = number + number_1 + number_2
print('Sum is: %s' % sum)
