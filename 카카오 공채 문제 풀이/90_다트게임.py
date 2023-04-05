def solution(dartResult):
    answer = 0
    
    bonus_check = False
    prev, cur = 0, ''
    for char in dartResult:
        if char.isdigit():
            if bonus_check:
                answer += prev
                prev, cur = cur, char
                bonus_check = False
            else:
                cur += char
        else:
            cur = int(cur)
            bonus_check = True
            
            if char == 'S':
                cur = pow(cur, 1)
            elif char == 'D':
                cur = pow(cur, 2)
            elif char == 'T':
                cur = pow(cur, 3)
            elif char == '*':
                prev *= 2
                cur *= 2
            elif char == '#':
                cur *= (-1)
    answer += prev
    answer += cur
    
    return answer
    
