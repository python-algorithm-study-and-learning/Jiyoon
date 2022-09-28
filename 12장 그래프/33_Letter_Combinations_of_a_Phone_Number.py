class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(i, temp):
            if len(temp) == len(digits):
                answer.append(temp)
                return
            
            for j in range(i, len(digits)):
                for char in numbers[digits[j]]:
                    dfs(j + 1, temp + char)
        
        numbers = {
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': []
        }
        
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return numbers[digits]
        
        answer = []
        dfs(0, '')
            
        return answer
