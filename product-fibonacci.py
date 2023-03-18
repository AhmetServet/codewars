def productFib(prod):
    a, b = 0, 1

    while a * b < prod:
        c = a + b
        a = b
        b = c

    return [a, b, a * b == prod]

