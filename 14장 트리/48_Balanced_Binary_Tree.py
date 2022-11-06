# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cp = True
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return -1
            
            left = dfs(node.left) + 1
            right = dfs(node.right) + 1
            
            if abs(left - right) > 1:
                self.cp = False
            
            return max(left, right)
        
        dfs(root)
        return self.cp
            
