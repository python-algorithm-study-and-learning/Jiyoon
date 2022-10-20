# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], length: int):
            if node is None:
                return length - 1
            
            left = dfs(node.left, length + 1)
            right = dfs(node.right, length + 1)
            if (left + right - length * 2) > max(left, right):
                answer.append(left + right - length * 2)
            return max(left, right)
        
        answer = []
        answer.append(dfs(root, 0))
        return max(answer)
