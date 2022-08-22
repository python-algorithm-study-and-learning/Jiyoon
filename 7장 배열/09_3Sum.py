class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else: 
                return []
        
        result = collections.defaultdict(int)
        nums_count = dict(collections.Counter(nums))
        
        nums = list(set(nums))
        nums.sort()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                # set 을 사용 -> [0, 0, 0, 0]가 [0]이 되는데, i + 1을 하면 제대로 못 세기 때문에 i부터 센다
                first = nums[i]
                second = nums[j]
                third = -(first + second)
                
                if first > 0 and second > 0:
                    break
                    
                nums_count[first] -= 1
                
                if nums_count[second] <= 0:
                    # j 가 i부터 시작하기 때문에, 개수가 하나인 경우에는 계산하지 않고 continue
                    continue
                nums_count[second] -= 1
                if nums_count.get(third) and nums_count[third] > 0:
                    # 중복이어도 같은 key값을 가지게 해서 따로 중복값 처리 x
                    result[tuple(sorted([first, second, third]))] += 1
                nums_count[first] += 1
                nums_count[second] += 1
        
        return result.keys()
