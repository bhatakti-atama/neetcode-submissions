# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        power = 1
        res = None
        ptr = None
        while l1 or l2 or carry != 0:
            d_sum = 0
            if l1 and l2:
                d_sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                d_sum = l1.val + carry
                l1 = l1.next
            elif l2:
                d_sum = l2.val + carry
                l2 = l2.next
            else:
                d_sum = carry
            if d_sum > 9:
                carry = 1
                d_sum -= 10
            else:
                carry = 0
            t = ListNode(d_sum, None)
            if res:
                ptr.next = t
                ptr = ptr.next
            else:
                res = t
                ptr = res
        return res