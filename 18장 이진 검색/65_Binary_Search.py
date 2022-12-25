class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        mid = (start + end) // 2

        while start <= end:
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                return mid
            
            mid = (start + end) // 2
        
        return -1
      
