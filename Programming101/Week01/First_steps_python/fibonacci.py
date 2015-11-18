def fibonacci(number):
    list_fib = [1, 1]

    for i in range(0, number - 2):
        next_digit = list_fib[i] + list_fib[i + 1]
        list_fib.append(next_digit)

    return list_fib


def fibonacci_rec(number):
    if number == 1 or number == 2:
        return 1
    return(fibonacci_rec(number - 1) + fibonacci_rec(number - 2))


print(fibonacci_rec(10))
