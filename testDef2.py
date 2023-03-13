# x = 20

# while x >= 0:
#     print(x)
#     x -= 1
# print('vce')


# for i in range(1, 11):
#     print(i*5)

# x = int(input('czyslo 1: '))
# y = int(input('czyslo 2: '))


# def mean(x, y):
#     result = x + y
#     return result


# s = mean(x, y)
# print(s)

# n = int(input('czyslo: '))


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)


# result = factorial(n)
# print("factorial czysla n: ", result)

# numbers = int(input("введіть числа: "))

numbers = list(map(int, input().split()))


def find_average(numbers):
    sum = 0
    count = 0
    for num in numbers:
        sum += num
        count += 1
    if sum == 0:
        return 0
    else:
        return sum / count


# numbers = [1, 2, 3, 10]
result = find_average(numbers)
print('Середнє арифметичне:', result)
