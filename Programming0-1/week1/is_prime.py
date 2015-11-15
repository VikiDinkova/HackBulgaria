from math import sqrt

n = int(input('Enter number: '))
sq_root_n = sqrt(n)
is_prime = True
start = 2
while start < sq_root_n:
    if n % start == 0:
        is_prime = False
        break
    start += 1
if is_prime:
    print('The number is prime')
else:
    print('The number is not prime')

