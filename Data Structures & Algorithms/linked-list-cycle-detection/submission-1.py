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
        fast = head.next
        slow = head

        # While fast and slow are not None
        while fast and slow:
            # If they are equal we have a loop
            if fast == slow:
                return True
            slow = slow.next
            for i in range(0, 2):
                if not fast:
                    return False
                fast = fast.next
        
        return False
