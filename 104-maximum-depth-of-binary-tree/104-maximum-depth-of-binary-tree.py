# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        queue = collections.deque()
        result = []
        max_count = 0
        queue.appendleft([root, 1])
        
        while queue:
            node, level = queue.popleft()
            if node.left:
                queue.appendleft([node.left, level+1])
            if node.right:
                queue.appendleft([node.right, level+1])
            max_count = max(max_count, level)
            
        return max_count
        
            
            
            
            
            
            
            
        