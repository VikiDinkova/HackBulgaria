a = int(input('Enter lower bound: '))
b = int(input('Enter upper bound: '))
x = int(input('Enter number: '))
if x == a:
    print('The number is equal to lower bound of the interval')
elif x == b:
    print('The nnumber is equal to upper bound of the interval')
elif a < x and x > b:
    print('The number is in the interval')
elif x < a:
    print('The number is outside the interval, x < lower bound')
else:
    print('The number is outside the interval x > upper bound')
