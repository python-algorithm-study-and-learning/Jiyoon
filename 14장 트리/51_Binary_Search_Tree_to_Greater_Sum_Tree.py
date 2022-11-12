# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def getGst(node: TreeNode, node_sum: int):
            if node is None:
                return node_sum
            
            node_sum = getGst(node.right, node_sum) + node.val
            node.val = node_sum
            
            return getGst(node.left, node_sum)
        
        getGst(root, 0)
        return root
            
