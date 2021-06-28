# Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
class Solution:
    # 연결 리스트 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
            
        return prev
            
    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> ListNode:
        list = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    # 파이썬 리스트를 연결 리스트로 변환
    def toReverseLinkedList(self, result):
        node = ListNode(result.pop())
        temp = node
        
        while result:
            temp.next = ListNode(result.pop())
            temp = temp.next
            
        return node
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        reverse_l1 = self.toList(self.reverseList(l1))
        reverse_l2 = self.toList(self.reverseList(l2))
        
        result = int(''.join(str(s) for s in reverse_l1)) + \
            int(''.join(str(s) for s in reverse_l2))
        
        return self.toReverseLinkedList(list(str(result)))
        
            
        
        