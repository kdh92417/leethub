# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = collections.deque()
        
        while head:
            lst.append(head.val)
            head = head.next
            
        while len(lst) > 1:
            if lst.popleft() != lst.pop():
                return False
            
        return True