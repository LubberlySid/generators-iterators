class EvenNumbers:
    def __init__(self, start, end):
        self.start = start if start % 2 == 0 else start + 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            current = self.start
            self.start += 2
            return current
        else:
            raise StopIteration


even_nums = EvenNumbers(1, 10)
for num in even_nums:
    print(num)
