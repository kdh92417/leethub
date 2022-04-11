# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        queue = collections.deque([root])
        
        while queue:
            cur = queue.popleft()
            left, right = None, None
            if cur.left:
                left = cur.left
                queue.append(cur.left)
                
            if cur.right:
                right = cur.right
                queue.append(cur.right)
                
            cur.left = right
            cur.right = left

        return root
                
        