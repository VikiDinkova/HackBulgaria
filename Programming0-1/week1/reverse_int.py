n = int(input('Enter number: '))
len_ = 0
temp = n
t = n
new = 0
while temp > 0:
    len_ += 1
    temp = temp // 10
while n > 0:
    t = n % 10
    new = new + t * (10 ** (len_ - 1))
    len_ = len_ - 1
    n = n // 10
print(new)
