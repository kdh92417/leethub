# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(head.val)
        root = ListNode(None, node)

        while head.next:
            head = head.next
            cur = ListNode(head.val)
            node = root
            # print('first while : ', node)

            while node:
                # print('inner while : ', node)
                if node.next and cur.val <= node.next.val:
                    cur.next = node.next  
                    node.next = cur
                    break

                elif not node.next:
                    node.next = cur
                    break
                    
                node = node.next
        
        return root.next
                    