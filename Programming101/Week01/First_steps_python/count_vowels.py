def count_vowels(str_):
	count = 0
	vowels = 'aeiouyAEIOUY'


	for i in str_:
		if i in vowels:
			count += 1
			
	return count


print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))