# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result: int = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def traverse(node):
            if node is not None:
                traverse(node.left)
                if node.val >= low and node.val <= high:
                    self.result += node.val
                traverse(node.right)
                
        traverse(root)
        
        return self.result
                