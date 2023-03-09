# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)


# factorial(5)
n = 50
k = 7


def factorial(n):

    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial(k):
    if k <= 1:
        return 1
    else:
        return k * factorial(k - 1)

    # c = factorial(n) / (factorial(n - k) * factorial(k))


def number_of_groups(n, k):
    result = factorial(n) / (factorial(n) - factorial(k)) * factorial(k)

    return int(result)
