search_word = input('Enter search word: ')
number_of_words = int(input('Enter number if inputs: '))
words = []
word_count = 0
while number_of_words > 0:
	current_word = input('')
	words += [current_word]
	number_of_words -= 1
for word in words:
	if search_word == word:
		word_count += 1
print('{0} is found {1} times'.format(search_word, word_count))