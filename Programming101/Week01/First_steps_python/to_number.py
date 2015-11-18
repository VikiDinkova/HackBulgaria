def to_number(digit_list):
    # digit = ''.join(digit_list)
    # return int(digit)

    number = 0
    power = len(digit_list) - 1

    for digit in digit_list:
        number += digit * (10 ** power)
        power -= 1

    return number


print(to_number([1, 2, 4]))