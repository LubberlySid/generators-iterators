class PalindromeIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0
        self.palindromes = self._find_palindromes()

    def _is_palindrome(self, word):
        return word == word[::-1]

    def _find_palindromes(self):
        palindromes = []
        for word in self.words:
            if self._is_palindrome(word):
                palindromes.append(word)
        return palindromes

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.palindromes):
            palindrome = self.palindromes[self.index]
            self.index += 1
            return palindrome
        else:
            raise StopIteration()


words_list = ['level', 'racecar', 'python', 'madam']
palindrome_iterator = PalindromeIterator(words_list)

for palindrome in palindrome_iterator:
    print(palindrome)



