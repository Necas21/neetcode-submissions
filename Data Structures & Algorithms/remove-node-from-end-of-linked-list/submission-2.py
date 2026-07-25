# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Pointers to track current and previous Nodes
        prev = None
        curr = head

        # Calculate length of list to wrap around
        list_length = 0
        while curr:
            list_length += 1
            curr = curr.next
        
        # Reset curr to head
        curr = head

        # Calculate new value of n
        n = list_length - n

        # Edge case where n == 0
        if n == 0:
            head = head.next
            return head

        # Iterate over list to find nth Node
        while n > 0:
            prev = curr
            curr = curr.next
            n -= 1

        # Remove link
        prev.next = curr.next

        return head