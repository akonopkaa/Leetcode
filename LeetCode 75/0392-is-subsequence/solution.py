class Solution:
    def isSubsequence(self, s, t):
        pointer = 0
        for char in t:
            if pointer == len(s):
                return True
            if char == s[pointer]:
                pointer += 1
        if pointer == len(s):
            return True
        else:
            return False
