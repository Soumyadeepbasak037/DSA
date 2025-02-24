def func(i, n):
    if (i > n):
        return
    print(i)
    func(i+1, n)


# func(0, 5)


def sum(i, add):
    if (i < 0):
        print(add)
        return
    sum(i-1, add+i)


sum(10, 0)
