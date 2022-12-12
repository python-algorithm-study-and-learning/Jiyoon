class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                print(nums_str[i], nums_str[j])
                if nums_str[i] + nums_str[j] < nums_str[j] + nums_str[i]:
                    nums_str[i], nums_str[j] = nums_str[j], nums_str[i]
                
        answer = ''.join(nums_str)
        if int(answer) == 0:
            return '0'

        return answer
        
