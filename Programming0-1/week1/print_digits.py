n = int(input('Enter number: '))
m = n
while m > 0:
    (n / 10 - n // 10) * 10
    m = n % 10
    print(m)
