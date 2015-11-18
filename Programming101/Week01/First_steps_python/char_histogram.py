def char_histogram(string_):
	dict_ = {}

	for item in string_:
		dict_[item] = string_.count(item)

	return(dict_)

print(char_histogram("AAAAaaa!!!"))