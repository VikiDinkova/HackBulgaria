from firstday import palindrome
import copy
from firstday import char_histogram


def is_number_balanced(n):
    n = str(n)
    first_part = sum([int(n[index]) for index in range(len(n) // 2)])
    last_part = sum([int(n[index])
                     for index in range((len(n) // 2) + 1, len(n))])

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


def prime_number(n):
    all_numbers = [x for x in range(2, n + 1)]
    for i in range(2, n + 1):
        not_prime = [x for x in range(i*2, n + 1, i)]
        all_numbers = set(all_numbers) - set(not_prime)
    return sorted(list(all_numbers))

# print(prime_number(50))


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
            if day in range(tupl[0], tupl[1] + 1):
                birthday_count += 1
        birthday_list.append(birthday_count)

    return birthday_list

# print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))


def sum_matrix(m):
    # suma = 0
    # for row in m:
    #     for col in row:
    #         suma += col
    # return suma

    return sum([col for row in m for col in row])

# print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def index_in_matrix(row, col, m):
    if col >= len(m) or col < 0 or row >= len(m[0]) or row < 0:
        return False
    return True


def get_neighbour_indexes(row, col):
    arr = [
        (row - 1, col - 1), (row, col - 1), (row + 1, col - 1),
        (row - 1, col), (row + 1, col),
        (row - 1, col + 1), (row, col + 1), (row + 1, col + 1)
    ]
    return arr


def matrix_bombing_plan(m):
    dict_ = {}
    for a in range(len(m)):
        for b in range(len(m[0])):
            temp_m = copy.deepcopy(m)
            tupl = (a, b)
            value = temp_m[a][b]
            neighbours = get_neighbour_indexes(a, b)
            for neighbour in neighbours:
                if index_in_matrix(neighbour[0], neighbour[1], temp_m):
                    if temp_m[neighbour[0]][neighbour[1]] <= value:
                        temp_m[neighbour[0]][neighbour[1]] = 0
                    else:
                        temp_m[neighbour[0]][neighbour[1]] -= value
            matrix_sum = sum_matrix(temp_m)
            dict_[tupl] = matrix_sum
    return dict_


# print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def is_transversal(trasversal, family):
    # count = 0

    # for element in trasversal:
    #     for tupl in family:
    #         count += tupl.count(element)

    # return count >= len(trasversal) and len(trasversal) == len(family)
    for group in family:
        it = [x for x in group if x in trasversal]

        if len(it) == 0 or len(it) > 1:
            return False

        return True


print(is_transversal((4, 5, 6), ((5, 7, 9), (1, 4, 3), (2, 6))))
print(is_transversal((1, 2), ((1, 5), (2, 3), (4, 7))))
print(is_transversal((2, 3, 4), ((1, 7), (2, 3, 5), (4, 8))))
