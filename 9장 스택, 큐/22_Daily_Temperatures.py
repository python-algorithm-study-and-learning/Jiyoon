class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # []가 list()보다 빠르다
        stack = []
        result = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
                
        return result
                
