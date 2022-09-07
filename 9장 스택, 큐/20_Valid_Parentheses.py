class Solution:
    def isValid(self, s: str) -> bool:
        char = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        
        s = list(reversed(s))
        print(s)
        stack = list()
        while s:
            temp = s.pop()
            if temp in char:
                stack.append(temp)
            else:
                if not stack or char.get(stack.pop()) != temp:
                    return False
        
        if stack:
            return False
        
        return True
            
