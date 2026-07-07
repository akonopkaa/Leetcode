class Solution:
    def productExceptSelf(self, nums):
        left = 1
        right = 1
        length = len(nums)
        answer = [1] * length
        i = 0
        while i < length:
            answer[i] = left
            left *= nums[i]
            i += 1
        i = len(nums) - 1
        while i >= 0:
            answer[i] *= right
            right *= nums[i]
            i -= 1
        return answer
