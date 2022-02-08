# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        result = ''
        while head:
            result += str(head.val)
            head = head.next
        
        total_int = 0
        for i, v in enumerate(result[::-1]):
            total_int += (2**i)*int(v)
            
        return total_int