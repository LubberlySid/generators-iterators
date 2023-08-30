class StringIterator:
    def __init__(self, user_string):
        self.user_string = user_string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.user_string):
            char = self.user_string[self.index]
            self.index += 1
            return char

        else:
            raise StopIteration


sentence = "Hello, World!"
str_iter = StringIterator(sentence)

for i in str_iter:
    print(i)
