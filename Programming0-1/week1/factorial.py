n = int(input('Enter number: '))
fact = 1
temp = n
while temp >= 1:
    fact = fact * temp
    temp -= 1
print('{0}! = {1}'.format(n, fact))
