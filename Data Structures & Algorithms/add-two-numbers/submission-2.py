# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        while l1 or l2:
            sum = carry
            if l1:
                sum = sum + l1.val
                l1 = l1.next
            if l2:
                sum = sum  + l2.val
                l2 =l2.next
            newNode = ListNode(sum%10)
            carry = sum//10
            curr.next = newNode
            curr = curr.next
        if carry:
            newNode1 = ListNode(carry)
            curr.next = newNode1
        return dummy.next  
