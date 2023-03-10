class Solution:
    cnt = collections.defaultdict(int)

    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        left = self.majorityElement(nums[:half])
        right = self.majorityElement(nums[half:])

        return [left, right][nums.count(right) > half]
