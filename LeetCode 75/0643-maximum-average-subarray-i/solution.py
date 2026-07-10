class Solution:
    def findMaxAverage(self, nums, k):
        i = 0
        j = k
        window = sum(nums[i:j])
        max_avg = window / k
        if len(nums) == 1:
            return nums[0]
        while j < len(nums):
            window = window - nums[i] + nums[j]
            a = window / k
            if a >= max_avg:
                max_avg = a
            i += 1
            j += 1
        return max_avg
