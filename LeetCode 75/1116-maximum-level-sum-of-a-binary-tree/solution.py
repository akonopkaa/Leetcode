# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root):
        if root.left is None and root.right is None:
            return 1
        max_sum = float("-inf")
        queue = [root]
        max_level = 1
        level = 1
        while queue:
            size = len(queue)
            sum = 0
            for _ in range(size):
                current = queue.pop(0)
                sum += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            if sum > max_sum:
                max_level = level
                max_sum = sum
            level += 1
        return max_level
