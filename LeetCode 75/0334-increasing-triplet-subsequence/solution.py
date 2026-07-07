class Solution:
    def increasingTriplet(self, nums):
        first_lowest = float('inf')
        second_lowest = float('inf')
        for i in range(len(nums)):
            if nums[i] < first_lowest:
                first_lowest = nums[i]
            elif nums[i] == first_lowest:
                continue
            elif nums[i] > first_lowest and nums[i] <= second_lowest:
                second_lowest = nums[i]
            else:
                return True
        return False
