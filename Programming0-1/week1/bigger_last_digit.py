n = int(input('Enter first number: '))
m = int(input('Enter second number: '))
n_last_digit = (n / 10) - (n // 10)
m_last_digit = (m / 10) - (m // 10)
if n_last_digit > m_last_digit:
    print(n)
elif m_last_digit > n_last_digit:
    print(m)
else:
    if n > m:
        print(n)
    elif n < m:
        print(m)
    else:
        print('The numbers are equal')
