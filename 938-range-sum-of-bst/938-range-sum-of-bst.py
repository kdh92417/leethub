# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.result = low + high
        def traverse(node):
            if node:
                if node.val > low and node.val < high:
                    self.result += node.val
                
                traverse(node.left)
                traverse(node.right)
        
        traverse(root)
        
        return self.result
                