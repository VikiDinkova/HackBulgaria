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
        elements = elements[len(take_same(elements)):]
    return arr
