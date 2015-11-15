n = int(input('Enter number: '))
sum_ = 0
while n > 0:
    last_dig = n - (n // 10) * 10
    sum_ = sum_ + last_dig
    n = n // 10
print(sum_)
    
    
