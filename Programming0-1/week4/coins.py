def calculate_coins(suma):
 	coins = [100, 50, 20, 10, 5, 2, 1]
 	dictionary = {'1': 0, '2': 0, 
 				'100': 0, '5': 0,
 				'10': 0, '50': 0, '20': 0}
 	suma = int(suma * 100)
 	for coin in coins:
 		dictionary[str(coin)] = suma // coin
 		suma = suma % coin
 		if suma == 0:
 			break
 	return dictionary


change = float(input('Enter float number: '))
print(calculate_coins(change))