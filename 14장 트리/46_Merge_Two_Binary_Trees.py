# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(node1: TreeNode, node2: TreeNode):
            if node1 is None and node2 is None:
                return None
            elif node1 is None:
                return node2
            elif node2 is None:
                return node1
            else:
                return TreeNode(node1.val + node2.val, merge(node1.left, node2.left), merge(node1.right, node2.right))
                
        root = merge(root1, root2)
        return root
        
        
