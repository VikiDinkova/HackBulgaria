def is_number_balanced(n):
    n = str(n)
    first_part = sum([int(n[index]) for index in range(len(n) // 2)])
    last_part = sum([int(n[index]) for index in range((len(n) // 2) + 1, len(n))])

    return first_part == last_part


# print(is_number_balanced(28471))


def is_increasing(seq):
    for index in range(len(seq) - 1):
        if seq[index] >= seq[index + 1]:

            return False

    return True

# print(is_increasing([1,2,3,4,5]))
# print(is_increasing([1]))
# print(is_increasing([5,6,-10]))
# print(is_increasing([1,1,1,1]))

def is_decreasing(seq):
    for index in range(len(seq) - 1):
        if seq[index] <= seq[index + 1]:

            return False

    return True


# print(is_decreasing([5,4,3,2,1]))
# print(is_decreasing([1,2,3]))
# print(is_decreasing([100, 50, 20]))
# print(is_decreasing([1,1,1,1]))


from firstday import palindrome

def get_largest_palindrome(n):
    n -= 1
 
    while n > 0:
        if palindrome(n):
            return n
        n -= 1

    return n


# print(get_largest_palindrome(99))
# print(get_largest_palindrome(252))
# print(get_largest_palindrome(994687))
# print(get_largest_palindrome(754649))


def prime_numbers(n):
    prime = []
    if n >= 3:
        prime.append(2)
        prime.append(3)
    for item in range(2, n):
        if item % 1 == 0 and item % item == 0 and item % 2 != 0 and item % 3 != 0:
            prime.append(item)
    return prime


# print(prime_numbers(30))


from firstday import char_histogram

def is_anagram(a, b):
    a = a.lower()
    b = b.lower()
    if len(a) != len(b):
        return False

    dict_a = char_histogram(a)
    dict_b = char_histogram(b)


    for i in dict_a:
        if dict_a[i] != dict_b[i]:
            return False
        else:
            continue
    return True


# print(is_anagram("BRADE", "BeaRD"))
# print(is_anagram("TOP_CODER", "COTO_PRODE"))


def birthday_ranges(birthday, ranges):
    birthday_list = []

    for tupl in ranges:
        birthday_count = 0

        for day in birthday:
            if day in range(tupl[0], tupl[1]+1):
                birthday_count += 1
        birthday_list.append(birthday_count)

    return birthday_list

# print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))
