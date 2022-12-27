class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
            
        index = nums.index(min(nums))
        pivot = len(nums) - index
        deque = collections.deque(nums)
        deque.rotate(pivot)
        left, right = 0, len(deque) - 1

        print(pivot)

        while left <= right:
            mid = (left + right) // 2
            if target == deque[mid]:
                return mid + index if mid < pivot else mid - pivot 
            elif target < deque[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
        
