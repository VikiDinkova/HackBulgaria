def winter_is_coming(seasons):
	counter = 0
	for season in seasons:
		if season != 'winter':
			counter += 1
		else:
			counter = 0
	if counter >= 5:
		return True
	else:
		return False

seasons = ["winter", "summer", "summer", "summer", "spring", "srping"]
print(winter_is_coming(seasons))