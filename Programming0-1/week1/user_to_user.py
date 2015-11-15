a = int(input('Enter a: '))
b = int(input('Enter b: '))
if a > b:
    c = a
    a = b
    b = c
while a <= b:
    print(a)
    a += 1
