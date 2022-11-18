# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def makeTree(nums: List[int]):
            if not pre or not nums:
                return None
            
            node_val = pre.popleft()
            index = nums.index(node_val)
            
            return TreeNode(node_val, makeTree(nums[:index]), makeTree(nums[index+1:]))
            
        pre = collections.deque(preorder)
        return makeTree(inorder)
