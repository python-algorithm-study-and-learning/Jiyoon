class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = list()
        
        temp = 1
        for num in nums:
            result.append(temp)
            temp *= num
        
        temp = 1
        for i in reversed(range(len(nums))):
            result[i] *= temp
            temp *= nums[i]
        
        return result
