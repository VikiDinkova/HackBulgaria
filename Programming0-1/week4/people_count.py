def get_people_count(activity):
	new_arr = []
	for person in activity:
		if person not in new_arr:
			new_arr.append(person)
	return len(new_arr)


people = ["Rado", "Ivo", "Maria", "Anneta", "Rado", "Rado", "Anneta", "Ivo", "Maria", "Rado"]
print(get_people_count(people))