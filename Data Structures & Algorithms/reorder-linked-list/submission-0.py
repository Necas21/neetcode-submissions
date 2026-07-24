# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# head -> 1 -> 2 -> 3 -> 4 -> 5 -> None
# head -> 1 -> 5 -> 2 -> 4 -> 3 -> None

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        tmp = head

        # Add all nodes to a list
        while tmp:
            nodes.append(tmp)
            tmp = tmp.next
        
        # Link nodes in the list using 2 pointers
        left = 0
        right = len(nodes) - 1

        # Iterate until pointers cross each other
        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            nodes[right].next = nodes[left]
            right -= 1
        
        # The final index of left will be the last position in the linked list
        # We need to set its next value to None to prevent an infinite loop
        nodes[left].next = None

