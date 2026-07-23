# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Empty list case
        if not head:
            return False

        # Initialise fast a slow pointer
        fast = head
        slow = head

        # While fast and fast.next are not None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            # If nodes are equal we are in a loop
            if fast == slow:
                return True
        
        return False
