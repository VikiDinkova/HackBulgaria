min = 0
max = 100
x = int(input('Enter the grade: '))
if x >= min and x <= 50:
    print('Слаб 2')
elif x >= 51 and x <= 60:
    print('Среден 3')
elif x >= 61 and x <= 70:
    print('Добър 4')
elif x >= 71 and x <= 80:
    print('Много добър 5')
elif x >= 81 and x < 100:
    print('Отличен 6')
elif x == 100:
    print('Много отличен 7')
else:
    print('Невалидни данни')
