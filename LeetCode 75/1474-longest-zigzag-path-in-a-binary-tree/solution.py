# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = 0

    def dfs(self, node, last, length):
        if node is None:
            return
        self.answer = max(self.answer, length)
        if last == 0:
            self.dfs(node.left, 0, 1)
            self.dfs(node.right, 1, length + 1)
        else:
            self.dfs(node.right, 1, 1)
            self.dfs(node.left, 0, length + 1)

    def longestZigZag(self, root):
        self.dfs(root, 0, 0)
        self.dfs(root, 1, 0)
        return self.answer
