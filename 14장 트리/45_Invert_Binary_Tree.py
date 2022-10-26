# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        queue = collections.deque([])
        queue.append(root)
        
        while queue:
            length = len(queue)
            
            while length:
                length -= 1
                node = queue.popleft()
                
                node.left, node.right = node.right, node.left
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
                    
        return root
            
