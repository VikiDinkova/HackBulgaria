def count_consonants(str_):
	count = 0
	consonants = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWZ'


	for i in str_:
		if i in consonants:
			count += 1
			
	return count

print(count_consonants("Theistareykjarbunga"))