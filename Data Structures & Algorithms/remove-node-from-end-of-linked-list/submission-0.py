# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head

        # Find length
        while temp is not None:
            temp = temp.next
            length += 1

        pos = length - n

        # If deleting head
        if pos == 0:
            return head.next

        temp = head
        count = 1

        # Go to node BEFORE the node we want to delete
        while count < pos:
            temp = temp.next
            count += 1

        # Delete target node
        temp.next = temp.next.next

        return head
        
