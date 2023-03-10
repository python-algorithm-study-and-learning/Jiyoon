class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        set_nums = set(nums)

        if len(set_nums) <= 1:
            return nums[0]
            
        prev = 0
        for x in set_nums:
            idx = nums.index(x)
            if idx - prev > len(nums) / 2:
                return nums[prev]
            prev = idx

        return nums[-1]
        
