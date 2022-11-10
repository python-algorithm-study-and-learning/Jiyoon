# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def makeBST(nums: List[int]) -> Optional[TreeNode]:
            if not nums:
                return None
            
            medium = len(nums) // 2
            return TreeNode(nums[medium], makeBST(nums[:medium]), makeBST(nums[medium+1:]))
        
        return makeBST(nums)
        
