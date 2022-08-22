class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_nums = [[i, nums[i]] for i in range(len(nums))]
        
        index_nums.sort(key=lambda x: x[1])
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            if index_nums[left][1] + index_nums[right][1] == target:
                return [index_nums[left][0], index_nums[right][0]]
            elif index_nums[left][1] + index_nums[right][1] > target:
                right -= 1
            else:
                left += 1
                
