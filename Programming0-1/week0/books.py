book1_name = "Pragmatic Thinking and Learning"
book1_price = 30
book2_name = "Learn Ypu a Haskell"
book2_price = 0
book3_name = "The healthy Programmer"
book3_price = 50
book4_name = "Code Complete"
book4_price = 60
book5_name = "The Pragmatic Programemr"
book5_price = 20
book6_name = "Pro Git"
book6_price = 0
book7_name = "Introduction to Algorithms"
book7_price = 80
book8_name = "Concrete Mathematics"
book8_price = 100
print(book1_name, book1_price)
print(book2_name, book2_price)
print(book3_name, book3_price)
print(book4_name, book4_price)
print(book5_name, book5_price)
print(book6_name, book6_price)
print(book7_name, book7_price)
print(book8_name, book8_price)
sum = book1_price + book2_price + book3_price + book4_price + book5_price + book6_price + book7_price + book8_price
print('Total: %d' %sum)
discount = 0.25
new_price = 0.25 * (book7_price + book8_price)
print('"Introduction to Algorithms" and "Concrete Mathematics" for: %d ' %new_price)
budget = 150
