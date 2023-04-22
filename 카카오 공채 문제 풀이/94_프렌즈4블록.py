import collections

def solution(m, n, board):
    answer = 0
    cnt = 0
    
    stacks = [[] for _ in range(n)]

    for i in range(n):
        for j in range(m-1, -1, -1):
            stacks[i].append(board[j][i])
    
    for stack in stacks:
        print(stack)
    
    while True:
        cnt = 0
        remove_list = list()
        for width in reversed(range(0, m - 1)):
            for height in range(0, n - 1):
                if not stacks[height][width].isalpha():
                    continue
                    
                rm_char = stacks[height][width].lower()
                if stacks[height][width+1].lower() == rm_char and stacks[height+1][width].lower() == rm_char and stacks[height+1][width+1].lower() == rm_char:
                    cnt += 1
                    
                    if stacks[height+1][width+1].isupper():
                        stacks[height+1][width+1] = rm_char
                        remove_list.append((height+1, width+1))
                        
                    if stacks[height+1][width].isupper():
                        stacks[height+1][width] = rm_char
                        remove_list.append((height+1, width))
                        
                    if stacks[height][width+1].isupper():
                        stacks[height][width+1] = rm_char
                        remove_list.append((height, width+1))
                    
                    if stacks[height][width].isupper():
                        stacks[height][width] = rm_char
                        remove_list.append((height, width))
            
        if not cnt:
            break
        else:
            for h, w in remove_list:
                del stacks[h][w]
                stacks[h].append(' ')
                answer += 1
    return answer
    
