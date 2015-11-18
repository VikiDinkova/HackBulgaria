def palindrome(obj):
    if str(obj) ==  str(obj)[::-1]:
        return True
    else:
        return False

print(palindrome(121))
print(palindrome("kapak"))
print(palindrome("baba"))