class Solution:
    def maxOperations(self, nums, k):
        nums.sort()
        i = 0
        j = len(nums) - 1
        count = 0
        while i < j:
            if (nums[i] + nums[j]) == k:
                i += 1
                j -= 1
                count += 1
            else:
                if (nums[i] + nums[j]) < k:
                    i += 1
                else:
                    j -= 1
        return count
