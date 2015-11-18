def count_words(words):
	dictionary = {}
	for word in words:
		if word not in dictionary.keys():
			dictionary[word] = 1
		else:
			dictionary[word] += 1
	return dictionary


arr = ["words", "are", "meaningful", "words", "words", "are"]
print(count_words(arr))