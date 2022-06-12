# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left, right = '', ''

        while l1:
            left = str(l1.val) + left
            l1 = l1.next
        
        while l2:
            right = str(l2.val) + right
            l2 = l2.next
        
        result = list(str(int(left) + int(right)))
        root = head = ListNode(None)
        # head.val = 3

        while result:
            head.next = ListNode(result.pop())
            head = head.next

        return root.next
        