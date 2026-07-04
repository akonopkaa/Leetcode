class Solution:
    def mergeAlternately(self, word1, word2):
        self.merged = []
        word1 = list(word1)
        word2 = list(word2)

        while word1 and word2:
            self.merged.append(word1.pop(0))
            self.merged.append(word2.pop(0))
        
        if word1:
            self.merged.extend(word1)
        else:
            self.merged.extend(word2)

        return "".join(self.merged)
