# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        lst = []
        p = head
        while p:
            lst.append(p.val)
            p = p.next
        
        lst.sort()
        p = head
        for v in lst:
            p.val = v
            p = p.next
        
        return head