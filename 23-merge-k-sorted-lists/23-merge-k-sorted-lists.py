# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        new_list = []
        root = answer = ListNode(None)
        for l in lists:
            while l:
                heapq.heappush(new_list, l.val)
                l = l.next
        
        
        while new_list:
            answer.next = ListNode(heapq.heappop(new_list))
            answer = answer.next
            
        return root.next