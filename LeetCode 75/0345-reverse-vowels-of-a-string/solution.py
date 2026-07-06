class Solution:
    def reverseVowels(self, s):
        string = list(s)
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        vowels_in_string = []
        for i, letter in enumerate(string):
            if letter in vowels:
                vowels_in_string.append(letter)
                string[i] = ""
        vowels_in_string.reverse()
        for i, letter in enumerate(string):
            if letter == "":
                string[i] = vowels_in_string.pop(0)
        return "".join(string)
