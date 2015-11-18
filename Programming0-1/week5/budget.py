def on_budget(books, budget):
	books = sorted(books)
	count_book = 0
	all_books = 0
	my_budget = budget
	dictionary= {}


	for book in books:
		if budget >= book:
			count_book += 1
		budget -= book
		all_books += book
	
	if count_book < len(books):
		loan = all_books - my_budget

	dictionary['books_on_budget'] = count_book
	dictionary['loan'] = loan
	return dictionary


books = [50, 60, 100]
budget = 20
print(on_budget(books,budget))