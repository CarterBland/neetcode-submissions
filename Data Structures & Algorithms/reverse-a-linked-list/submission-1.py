# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lastNode = None

        while head:
            current = head
            head = head.next
            current.next = lastNode
            lastNode = current


        return lastNode