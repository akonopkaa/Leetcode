class Solution:
    def moveZeroes(self, nums):
        i = 0
        counter = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[counter], nums[i] = nums[i], nums[counter]
                counter += 1
            i += 1
