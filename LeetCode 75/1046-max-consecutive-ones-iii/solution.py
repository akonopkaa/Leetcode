class Solution:
    def longestOnes(self, nums, k):
        left = 0
        right = 0
        zeroes = 0
        max_count = 0
        while right < len(nums):
            if nums[right] == 0:
                zeroes += 1
            if zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            max_count = max(max_count, right - left + 1)
            right += 1
        return max_count
