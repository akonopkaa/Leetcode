# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSum(self, root, targetSum):
        if root is None:
            return 0
        
        def dfs(node, remaining):
            count = 0
            if node is None:
                return 0
            remaining = remaining - node.val
            if remaining == 0:
                count += 1
            count += dfs(node.left, remaining)
            count += dfs(node.right, remaining)

            return count

        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
