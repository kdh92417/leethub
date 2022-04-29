# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cnt: int = 0
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def traverse(node):
            if node is not None:
                traverse(node.right)
                self.cnt += node.val
                node.val = self.cnt
                traverse(node.left)
        
        traverse(root)
        return root