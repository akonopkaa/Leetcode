# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head):
        if head.next is None:
            return None
        slow = fast = head
        pre_slow = post_slow = slow
        while fast and fast.next is not None:
            pre_slow = slow
            slow = slow.next
            post_slow = slow.next
            fast = fast.next.next
        pre_slow.next = post_slow
        return head
