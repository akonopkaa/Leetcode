# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        if root is None:
            return []
        result = [root.val]
        queue = [root]
        while queue:
            size = len(queue)
            last = None
            for _ in range(size):
                current = queue.pop(0)
                if current.left:
                    queue.append(current.left)
                    last = current.left.val
                if current.right:
                    queue.append(current.right)
                    last = current.right.val
            if last is not None:
                result.append(last)
        return result
