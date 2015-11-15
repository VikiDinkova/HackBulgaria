import time
today = time.strftime('%A')
print(today)
if today == 'Friday':
    print('Today is Friday')
else:
    print('It is not Friday ;( Today is {0}'.format(today))
