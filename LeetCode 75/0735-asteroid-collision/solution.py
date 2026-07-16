class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for char in asteroids:
            if char > 0:
                stack.append(char)
            else:
                removed_both = False
                while stack and stack[-1] > 0:
                    if stack[-1] < abs(char):
                        stack.pop()
                    elif stack[-1] == abs(char):
                        stack.pop()
                        removed_both = True
                        break
                    else:
                        break
                if not removed_both and (len(stack) == 0 or stack[-1] < 0):
                    stack.append(char)
        return stack
