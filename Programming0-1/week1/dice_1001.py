from random import randint

sum_maria = 1001
sum_ivan = 1001
while True:
    roll = 5
    sum_roll_maria = 0
    sum_roll_ivan = 0
    while roll > 0:
        roll_maria = randint(1, 6)
        sum_roll_maria += roll_maria
        roll_ivan = randint(1,6)
        sum_roll_ivan += roll_ivan
        roll -= 1

    print('Maria rolls: {0}'.format(sum_roll_maria))
    print('Ivan rolls: {0}'.format(sum_roll_ivan))
    if sum_maria > 0:
        sum_maria -= sum_roll_maria
    elif sum_maria < 0:
        sum_maria += sum_roll_maria
    print('Maria\'s sum : {0}'.format(sum_maria))
    if sum_maria == 0:
        print('Maria is a winner!')
        break

    if sum_ivan > 0:
        sum_ivan -= sum_roll_ivan
    elif sum_ivan < 0:
        sum_ivan += sum_roll_ivan
    print('Ivan\'s sum: {0}'.format(sum_ivan))
    if sum_ivan == 0:
        print('Ivan is a winner! ')
        break
