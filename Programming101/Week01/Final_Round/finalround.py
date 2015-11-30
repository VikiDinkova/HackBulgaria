def count_words(arr):
    dict_ = {}
    for element in arr:
        dict_[element] = arr.count(element)
    return dict_

# print(count_words(["apple", "banana", "apple", "pie"]))
# print(count_words(["python", "python", "python", "ruby"]))


def nan_expand(times):
    str_ = ''
    if times >= 1:
        str_ += 'Not '
    while times > 1:
        str_ += 'a Not '
        times -= 1
    if times == 1:
        str_ += 'a NaN '
    return str_


# print(nan_expand(0))
# print(nan_expand(1))
# print(nan_expand(2))
# print(nan_expand(3))

def iterations_of_nan_expand(expanded):
    if 'Not' not in expanded and expanded != '':
        return False
    a = expanded.count('Not')
    return a

# print(iterations_of_nan_expand(""))
# print(iterations_of_nan_expand("Not a NaN"))
# print(iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
# print(iterations_of_nan_expand("Show these people!"))


# def group(things):
#     big_list = []

#     for thing in range(len(things) - 1):
#         small_list = []
#         big_list.append(things[thing])

#         if things[thing] == things[thing + 1]:
#             small_list.append(things[thing])
#             small_list.append(things[thing])

#     big_list.append(small_list)
#     return big_list


# print(group([1, 1, 1, 2, 3, 1, 1]))
# print(group([1, 2, 1, 2, 3, 3]))

def take_same(a):
    arr = [a[0]]

    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            arr.append(a[i + 1])
        else:
            return arr

    return arr


def group(elements):
    arr = []

    while len(elements) > 0:
        arr.append(take_same(elements))
        # print('arr {0}'.format(arr))
        elements = elements[len(take_same(elements)):]
        # print('elements {0}'.format(elements))

    return arr

# print(group([1, 1, 1, 2, 3, 1, 1]))
# print(group([1, 2, 1, 2, 3, 3]))
# print(group([1, 1, 1, 2, 3, 3, 1, 1]))
# print(take_same([1,1]))


def max_consecutive(items):
    items = group(items)
    largest_len = 0
    for item in items:
        if largest_len < len(item):
            largest_len = len(item)
    return largest_len

# print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
# print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))


def gas_stations(distance, tank_size, stations):
    gas_stops = []
    temp_tank_size = tank_size
    stations = [0] + stations + [distance]
    for i in range(len(stations) - 1):
        gas_burned = stations[i + 1] - stations[i]
        if temp_tank_size > gas_burned:
            temp_tank_size -= gas_burned
        else:
            gas_stops.append(stations[i])
            temp_tank_size = tank_size
            temp_tank_size -= gas_burned

    return gas_stops

# print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
# print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))


# import re


# def sum_of_numbers(st):
#     nums = re.findall(r'\d+', st)
#     sum_ = 0
#     for num in nums:
#         sum_ += int(num)
#     return sum_


def sum_of_numbers(st):
    sum_ = 0
    first_index = 0
    last_index = 0

    for i in range(len(st)):
        if st[i].isdigit() and first_index == 0:
            first_index = i
        if not st[i].isdigit() and first_index != 0:
            last_index = i
            sum_ += int(st[first_index:last_index])
            first_index = 0
            last_index = 0
        if st[i].isdigit() and first_index != 0 and i == len(st) - 1:
            last_index = i + 1
            sum_ += int(st[first_index:last_index])
            first_index = 0
            last_index = 0

    return sum_


# print(sum_of_numbers("ab125cd3"))
# print(sum_of_numbers("ab12"))
# print(sum_of_numbers("ab"))


# 100 SMS
def array_to_symbol(group_list):
    buttons = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i'],
        ['j', 'k', 'l'],
        ['m', 'n', 'o'],
        ['p', 'q', 'r', 's'],
        ['t', 'u', 'v'],
        ['w', 'x', 'y', 'z']
    ]

    count = len(group_list)
    button = buttons[group_list[0] - 2]
    symbol_index = count % len(button) - 1

    return button[symbol_index]


def numbers_to_message(press_sequence):
    string = ''
    is_cap = False
    groups = group(press_sequence)

    for group_ in groups:
        if group_[0] == -1:
            continue
        elif group_[0] == 1:
            is_cap = True
        elif group_[0] == 0:
            string += ' '
        else:
            if is_cap:
                string += array_to_symbol(group_).upper()
                is_cap = False
            else:
                string += array_to_symbol(group_)

    return string

print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))
print(numbers_to_message([2, 2, 2, 2]))
print(numbers_to_message(
    [1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]
))


def symbol_to_list(letter):
    buttons = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i'],
        ['j', 'k', 'l'],
        ['m', 'n', 'o'],
        ['p', 'q', 'r', 's'],
        ['t', 'u', 'v'],
        ['w', 'x', 'y', 'z']
    ]

    for button in buttons:

        if letter in button:
            push_button = buttons.index(button) + 2
            press = button.index(letter) + 1
            return [push_button for i in range(press)]


def are_symbols_from_same_button(a, b):
    buttons = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i'],
        ['j', 'k', 'l'],
        ['m', 'n', 'o'],
        ['p', 'q', 'r', 's'],
        ['t', 'u', 'v'],
        ['w', 'x', 'y', 'z']
    ]

    for button in buttons:
        if a in button and b in button:

            return True

    return False


def message_to_numbers(message):
    sequence = []
    previous_symbol = ''

    for symbol in message:
        if symbol == ' ':
            sequence.append(0)
        else:
            if are_symbols_from_same_button(previous_symbol.lower(), symbol.lower()):
                sequence.append(-1)
            if symbol == symbol.upper():
                sequence.append(1)
                sequence += symbol_to_list(symbol.lower())
            else:
                sequence += symbol_to_list(symbol)
        previous_symbol = symbol

    return sequence


print(message_to_numbers("aAabbcda"))
print(message_to_numbers("Ivo e panda"))
print(message_to_numbers("aabbcc"))
