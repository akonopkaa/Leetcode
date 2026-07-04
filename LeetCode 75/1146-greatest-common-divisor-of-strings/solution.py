class Solution:
    def gcdOfStrings(self, str1, str2):

        if len(str1) <= len(str2):
            self.shorter = str1
            self.longer = str2
        else:
            self.shorter = str2
            self.longer = str1
        i = len(self.shorter) - 1

        while i >= 0:
            if len(str1) % len(self.shorter) != 0 or len(str2) % len(self.shorter) != 0:
                self.shorter = self.shorter[:i]
                i -= 1
                continue
            for j in range(len(self.longer) // len(self.shorter)):
                if self.longer[j * len(self.shorter):(j + 1) * len(self.shorter)] != self.shorter:
                    break
            else:
                for j in range(len(str1) // len(self.shorter)):
                    if str1[j * len(self.shorter):(j + 1) * len(self.shorter)] != self.shorter:
                        break
                else:
                    for j in range(len(str2) // len(self.shorter)):
                        if str2[j * len(self.shorter):(j + 1) * len(self.shorter)] != self.shorter:
                            break
                    else:
                        return self.shorter
            self.shorter = self.shorter[:i]
            i -= 1
        return ""
    
solution = Solution()
print(solution.gcdOfStrings("ABABAB", "ABAB"))
