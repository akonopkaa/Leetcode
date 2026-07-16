class Solution:
    def decodeString(self, s):
        stack = []
        nums = ""
        chars = ""
        for char in s:
            if char != "]":
                stack.append(char)
            if char == "]":
                nums = ""
                chars = ""
                while stack[-1] != "[":
                    chars += stack.pop()
                stack.pop()
                while stack and stack[-1].isnumeric():
                    nums += stack.pop()
                decoded = int(nums[::-1]) * chars[::-1]
                stack.extend(decoded)
        return "".join(stack)

