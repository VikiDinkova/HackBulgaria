def max_score(beers, fries):
	arr_count = []
	for beer in beers:
		for fry in fries:
			count = beer * fry
			arr_count.append(count)

	return max(arr_count)


print('The max score is: {0}'.format(max_score([10, 11], [1, 5])))
