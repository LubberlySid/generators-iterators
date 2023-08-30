def even_odd_generator(number):
    numbers_list = list(range(1, number + 1))

    for i in numbers_list:
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"

        elif i % 3 == 0:
            yield "Fizz"

        elif i % 5 == 0:
            yield "Buzz"

        else:
            yield i

        i += 1


generator = even_odd_generator(15)
for num in generator:
    print(num)
