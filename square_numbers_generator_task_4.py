def square_numbers(number):
    numbers_list = list(range(1, number + 1))
    for i in numbers_list:
        nums = i * i
        yield nums
        i += 1


generator = square_numbers(5)
for num in generator:
    print(num)
