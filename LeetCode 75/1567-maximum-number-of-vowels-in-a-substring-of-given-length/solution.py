class Solution:
    def maxVowels(self, s, k):
        left = 0
        right = k
        vowels = list("aeiou")
        count = 0
        for char in s[:k]:
            if char in vowels:
                count += 1
        max_count = count
        while right < len(s):
            if s[right] in vowels:
                count += 1
            if s[left] in vowels:
                count -= 1
            max_count = max(count, max_count)
            left += 1
            right += 1
        return max_count
