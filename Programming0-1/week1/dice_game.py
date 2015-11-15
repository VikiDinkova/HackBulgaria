from random import randint


sides = input('Enter dice sides: ')
sides = int(sides)
player1 = input('Enter player 1 name: ')
player2 = input('Enter player 2 name: ')
roll1 = randint(1, sides)
roll2 = randint(1, sides)
print('%s rolls %s' %(player1, roll1))
print('%s rolls %s' %(player2, roll2))
if roll1 > roll2:
    print('%s wins!' % player1)
elif roll1 < roll2:
    print('%s wins!' % player2)
else:
    print('Equality')
