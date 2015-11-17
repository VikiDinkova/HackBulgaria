string = input('Enter a sentence: ')
vowels = 'aeiouyAEIOUY'
counter = 0

for letter in string:
	if letter in vowels:
		counter += 1
print(counter)