# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        result = ''
        l1_st = ''
        l2_st = ''
    
        while l1 or l2:
            if l1:
                l1_st = str(l1.val) + l1_st
                l1 = l1.next
            if l2:
                l2_st = str(l2.val) + l2_st
                l2 = l2.next
            
        result = list(str(int(l1_st)+int(l2_st)))
        cur = int(result.pop())
        l = ListNode(val=cur)
        temp = l
        while result:
            cur = int(result.pop())
            temp.next = ListNode(cur)
            temp = temp.next
            
        return l
            
        
        