# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        answer = []
        
        while head:
            answer.append(head.val)
            head = head.next
            
        answer.sort(reverse=True)
        head = root = ListNode(answer.pop())
        
        while answer:
            root.next = ListNode(answer.pop())
            root = root.next
        
        return head