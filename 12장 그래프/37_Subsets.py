class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i:int, subset: List[int]):
            answer.append(subset)
            
            for j in range(i, len(nums)):
                dfs(j + 1, subset + [nums[j]])
                
        answer = []
        dfs(0, [])
            
        return answer
