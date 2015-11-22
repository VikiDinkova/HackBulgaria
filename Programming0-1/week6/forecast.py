def forecast(days):
	count_rain = 0
	count_snow = 0
	count_sunshine = 0
	for day in days:
		if day == 'rain':
			count_rain += 1
		elif day == 'snow':
			count_snow += 1
		elif day == 'sunshine':
			count_sunshine += 1
		else:
			print('Invalid day')
	if count_rain > count_sunshine and count_rain > count_snow:
		return 'rain'
	if count_sunshine > count_rain and count_sunshine > count_snow:
		return 'sunshine'
	if count_snow > count_sunshine and count_snow > count_rain:
		return 'snow'
	if count_rain == count_snow and count_rain > count_sunshine:
		return 'sunshine'
	if count_rain == count_sunshine and count_rain > count_snow:
		return 'snow'
	if count_snow == count_sunshine and count_snow > count_rain:
		return 'rain'
	if count_rain == count_sunshine == count_snow:
		return days[len(days) - 1]


days1 = ["snow", "snow", "rain", "sunshine"]
days2= ["rain", "rain", "snow", "snow", "sunshine", "sunshine"]
days3 = ["rain", "rain", "sunshine", "sunshine"]
print(forecast(days1))
print(forecast(days2))
print(forecast(days3))