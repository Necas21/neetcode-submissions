# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# head -> 0 -> 1 -> 2 -> 3

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If head is empty
        if not head:
            return head

        curr_node = head
        next_node = head.next
        head.next = None

        while next_node:
            tmp = next_node.next
            next_node.next = curr_node
            curr_node = next_node
            next_node = tmp
        
        return curr_node