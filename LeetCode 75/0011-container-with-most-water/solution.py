class Solution:
    def maxArea(self, height):
        max_area = 0
        i = 0
        j = len(height) - 1
        while i <= j:
            a = (min(height[i], height[j])) * (j - i)
            if a >= max_area:
                max_area = a
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max_area
