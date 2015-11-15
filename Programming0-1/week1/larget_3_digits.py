n = int(input('Enter number: '))
a = n % 10
b = (n // 10) % 10
c = n // 100
if a >= b and a >= c:
    if b >= c:
        print(a * 100 + b * 10 + c)
    else:
        print(a * 100 + c * 10 + b)
elif b >= a and b >= c:
    if a >= c:
        print(b * 100 + a * 10 + c)
    else:
        print(b * 100 + c * 10 + a)
elif c >= a and c >= b:
    if a >= b:
        print(c * 100 + a * 10 + b)
    else:
        print(c * 100 + b * 10 + a)

if a <= b and a <= c:
    if b <= c:
        print(a * 100 + b * 10 + c)
    else:
        print(a * 100 + c * 10 + b)
elif b <= a and b <= c:
    if a <= c:
        print(b * 100 + a * 10 + c)
    else:
        print(b * 100 + c * 10 + a)
elif c <= a and c <= b:
    if a <= b:
        print(c * 100 + a * 10 + b)
    else:
        print(c * 100 + b * 10 + a)    
