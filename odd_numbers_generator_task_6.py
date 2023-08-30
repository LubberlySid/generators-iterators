def odd_numbers(numbers_list):
    odd_numbers_list = []
    for number in numbers_list:
        if number % 2 == 1:
            odd_numbers_list.append(number)
            number += 1
    yield odd_numbers_list


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_nums = odd_numbers(numbers)
for num in odd_nums:
    print(num)
