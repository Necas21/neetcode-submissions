# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # If list1 is empty
        if not list1:
            return list2

        # If list2 is empty
        if not list2:
            return list1

        # Find head of the list
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        # Pointer to current minimum value
        curr = head

        # Iterate over both lists until None
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next
        
        # If list1 is empty we have reached the end so we set next to the rest of list2
        if not list1:
            curr.next = list2
        
        if not list2:
            curr.next = list1

        return head