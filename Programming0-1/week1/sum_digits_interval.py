n = int(input('Enter n: '))
m = int(input('Enter m: '))
while n <= m:
    sum_ = 0
    temp = n
    while temp > 0:
        last_digit = temp - (temp // 10) * 10
        sum_ = sum_ + last_digit
        temp = temp // 10
    print('Sum of {0} is: {1}'.format(n, sum_))
    n += 1
