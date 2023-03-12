class Solution:
    def calculate(self, left, right, operator):
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right

    def diffWaysToCompute(self, expression: str) -> List[int]:
        def divideConquer(expression):
            if expression.isdigit():
                return [int(expression)]
            
            output = []

            for i in range(len(expression)):
                if expression[i] in ['+', '-', '*']:
                    lefts =  divideConquer(expression[:i])
                    rights = divideConquer(expression[i+1:])

                    for left in lefts:
                        for right in rights:
                            output.append(self.calculate(left, right, expression[i]))
            
            return output
        
        return divideConquer(expression)
        
