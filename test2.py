while True:

    n = int(input('Enter numer: '))

    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return (fibonacci(n-1) + fibonacci(n-2))

    print("Result fibo: ")
    for i in range(n):

        print(fibonacci(i))

    continue
