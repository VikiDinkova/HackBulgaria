a = int(input('Enter a: '))
b = int(input('Enter b: '))
oper = input('Enter operation: ')
if oper == '+':
    c = a + b
elif oper == '-':
    c = a - b
elif oper == '*':
    c = a * b
elif oper == '/':
    c = a / b
else:
    print('We do not support that operation.')
print(c)
