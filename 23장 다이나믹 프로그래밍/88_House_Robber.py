class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return nums[0]

        dp = collections.defaultdict(int)
        for i, num in enumerate(nums):
            if i == 0 or i == 1:
                dp[i] = num
            
            if i == 2:
                dp[i] = max(dp[i - 2], num)

            dp[i] = max(dp[i - 2], dp[i - 3]) + num

        return max(dp[length - 1], dp[length - 2])
        
