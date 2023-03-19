class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        results = []
        cur = 0
        for num in nums:
            cur = max(num, cur + num)
            results.append(cur)
        
        return max(results)
      
