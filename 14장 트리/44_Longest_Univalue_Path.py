# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, value: int):
            if node is None:
                 return -1
            
            if node.val != value:
                queue.append(node)
                return -1
            
            left = dfs(node.left, value) + 1
            right = dfs(node.right, value) + 1
            if (left + right) > max(left, right):
                answer.append(left + right)
            
            return max(left, right)
        
        if root is None:
            return 0
        answer = []
        queue = collections.deque([])
        queue.append(root)
        while queue:
            node = queue.popleft()
            answer.append(dfs(node, node.val))
            
        return max(answer)
