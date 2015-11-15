n = int(input('Enter number: '))
count = 0
sum_ = 0
while count < n:
    if count % 2 == 0:
        sum_ = sum_ + count
    count += 1
print(sum_)
