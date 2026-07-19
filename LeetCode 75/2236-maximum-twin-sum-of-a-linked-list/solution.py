# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head):
        slow = fast = head
        first_stack = []
        second_stack = []
        while fast and fast.next is not None:
            first_stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        head = slow
        while slow:
            second_stack.append(slow.val)
            slow = slow.next
        second_stack.reverse()
        max_pair = float("-inf")
        for i in range(len(first_stack)):
            max_pair = max(max_pair, first_stack[i] + second_stack[i])
        return max_pair
        
