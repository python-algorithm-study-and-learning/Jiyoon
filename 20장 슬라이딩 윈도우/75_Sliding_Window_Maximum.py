# 시간초과
# 책에 있는 풀이도 시간 초과,,

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_list = []

        for i in range(len(nums) - k + 1):
            max_list.append(max(nums[i:i+k]))

        return max_list
        
