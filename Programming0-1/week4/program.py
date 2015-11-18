first_name = input('Enter first name: ')
second_name = input('Enter second name: ')
third_name = input('Enter third name: ')
birth_year = int(input('Enter birth year: '))

dictionary = {}

dictionary['first_name'] = first_name
dictionary['second_name'] = second_name
dictionary['third_name'] = third_name
dictionary['birth_year'] = birth_year
dictionary['current_age'] = 2015 - birth_year

print(dictionary)