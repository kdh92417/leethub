# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        new_list = []
        root = answer = ListNode(None)
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(new_list, (lists[i].val, i, lists[i]))
                
        while new_list:
            node = heapq.heappop(new_list)
            idx = node[1]
            answer.next = node[2]
            
            answer = answer.next
            if answer.next:
                heapq.heappush(new_list, (answer.next.val, idx, answer.next))
                
        return root.next