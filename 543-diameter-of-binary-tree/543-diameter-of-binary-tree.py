# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0
        
        def search_level(node):
            if not node:
                return 0
            
            left = 1 + search_level(node.left)
            right = 1 + search_level(node.right)
            
            return max(left, right)
            
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
            diameter = max(diameter, search_level(node.left) + search_level(node.right))
                
        return diameter
        
        