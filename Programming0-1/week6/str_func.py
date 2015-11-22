def change_at(index, ch, string):
    result = ""
    n = len(string)

    for str_index in range(0, n):
        if str_index == index:
            result += ch
        else:
            result += string[str_index]

    return result

print(change_at(0, "i", 'aaa'))

def reverse(string):
	return string[::-1]

print(reverse('mama'))

def join(delimiter, items):
	temp = ''
	for el_index in range(len(items)):
		if el_index == len(items) - 1:
			temp += items[el_index]
			return temp
		temp += items[el_index] + delimiter
	return temp

print(join('/', ["Radoslav", "Yordanov", "Georgiev"]))

def startwith(search, string):
	i = 0
	while i < len(search):
		if string[i] != search[i]:
			return False
		i += 1
	return True

print(startwith('Pt', 'Python'))

def endswith(search, string):
	i = len(search) - 1
	j = len(string) - 1
	while i >= 0:
		if string[j] != search[i]:
			return False
		i -= 1
		j -= 1
	return True

print(endswith('.py', 'hello.py'))

def endswith_2(search, string):
	temp_search = reverse(search)
	temp_string = reverse(string)
	return startwith(temp_search, temp_string)

def trim(string):
	first_index = 0
	last_index = 0
	for i in range(len(string)):
		if string[i] != ' ':
			first_index = i
			break
	for i in range(len(string)-1, -1, -1):
		if string[i] != ' ':
			last_index = i
			break
	return string[first_index:last_index+1]

print(trim("   asd   "))



