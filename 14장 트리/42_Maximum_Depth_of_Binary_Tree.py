# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            temp = collections.deque()
            depth += 1
            while queue:
                node = queue.popleft()
                if node is None:
                    continue
            
                temp.append(node.left)
                temp.append(node.right)
            queue = temp
            
        return depth - 1
