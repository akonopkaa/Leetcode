class Solution:
    def reverseWords(self, s):
        s = s.split()
        for word in s:
            word = word.strip()
        s.reverse()
        return " ".join(s)
