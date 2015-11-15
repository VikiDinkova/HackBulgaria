a = int(input('Enter a: '))
b = int(input('Enter b: '))
if a > b:
    c = a
    a = b
    b = c
while a <= b:
    if a % 2 == 0:
        print('%s - even' %a)
    else:
        print('%s- odd' %a)
    a += 1
    
