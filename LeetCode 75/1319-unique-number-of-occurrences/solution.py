class Solution:
    def uniqueOccurrences(self, arr):
        nums_dict = {}
        nums = []
        nums_set = {}
        for a in arr:
            if a in nums_dict:
                nums_dict[a] += 1
            else:
                nums_dict[a] = 1
        for num in nums_dict.values():
            nums.append(num)
        nums_set = set(nums)
        if(len(nums) == len(nums_set)):
            return True
        else:
            return False
