class Solution:
    def findDifference(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        distinct1 = set1 - set2
        distinct2 = set2 - set1
        answer = []
        answer.append(list(distinct1))
        answer.append(list(distinct2))
        return answer
