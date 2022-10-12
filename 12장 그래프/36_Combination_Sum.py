class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i: int, nums: List[int]):
            if sum(nums) == target:
                answer.append(nums)
                return
            elif sum(nums) > target:
                return
            else:
                for j in range(i, len(candidates)):
                    dfs(j, nums + [candidates[j]])
                    
        answer = []
        for idx in range(len(candidates)):
            dfs(idx, [candidates[idx]])
            
        return answer
