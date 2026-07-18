# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None or head.next.next is None:
            return head
        odd = head
        even = head.next
        even_start = even
        while odd and odd.next is not None and even and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_start
        return head
