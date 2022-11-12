# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def getSum(node: TreeNode, isLow: bool, isHigh: bool):
            if node is None:
                return 0
            
            if isLow and isHigh: # 아직 갈라지지 않은 경우
                if low < node.val and high < node.val:      # low, high가 현재 노드보다 작은 경우
                    return getSum(node.left, True, True)
                elif low > node.val and high > node.val:    # low, high가 현재 노드보다 큰 경우
                    return getSum(node.right, True, True)
                else:                                       # 현재 노드를 기점으로 low와 high가 갈라지는 경우
                    return node.val + getSum(node.left, True, False) + getSum(node.right, False, True)
            elif isLow: # 갈라져서 low를 체크하는 부분
                if low == node.val:     # 현재 노드의 값이 low와 같은 경우, 현재 노드의 오른쪽 자식을 합해줌
                    return node.val + dfs(node.right)
                elif low < node.val:    # 현재 노드의 값이 low보다 큰 경우, 왼쪽에서 low를 찾되 현재 노드의 오른쪽 자식을 합해줌
                    return node.val + getSum(node.left, True, False) + dfs(node.right)
                else:                   # 현재 노드의 값이 low보다 작은 경우 현재 노드값 포함 X
                    return getSum(node.right, True, False)
            elif isHigh: # 갈라져서 right를 체크하는 부분
                if high == node.val:    # 현재 노드의 값이 high와 같은 경우, 현재 노드의 왼쪽 자식을 합해줌
                    return node.val + dfs(node.left)
                elif high < node.val:   # 현재 노드의 값이 high보다 큰 경우 현재 노드값 포함 X
                    return getSum(node.left, False, True)
                else:                   # 현재 노드의 값이 high보다 작은 경우, 오른쪽에서 high를 찾되 현재 노드의 왼쪽 자식을 합해줌
                    return node.val + getSum(node.right, False, True) + dfs(node.left)
        
        def dfs(node:TreeNode):
            if node is None:
                return 0
            
            return node.val + dfs(node.left) + dfs(node.right)
            
        return getSum(root, True, True)
        
        
