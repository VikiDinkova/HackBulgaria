def status_count(students):
	dictionary = {'finalized': [], 'not_finalized': []}
	for student in students:
		if student['status'] == 'not_finalized':
			dictionary['not_finalized'].append(student['name'])
		if student['status'] == 'finalized':
			dictionary['finalized'].append(student['name'])
	return dictionary


students = [{
              "name": "RadoRado",
              "status": "not_finalized"
            }, {
              "name": "Ivo",
              "status": "finalized"
            }, {
              "name": "Genadi",
              "status": "finalized"
            }]

print(status_count(students))