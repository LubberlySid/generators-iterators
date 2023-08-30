def fibonacci_numbers():
    number1, number2 = 0, 1
    while True:
        yield number1
        number1, number2 = number2, number1 + number2


fib_gen = fibonacci_numbers()
for i in range(10):
    print(next(fib_gen))
