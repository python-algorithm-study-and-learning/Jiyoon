def solution(n, arr1, arr2):
    map = [arr1[i] | arr2[i] for i in range(n)]
    answer = []
    for i in range(n):
        answer.append(dex_to_str(n, arr1[i] | arr2[i]))
    
    return answer

def dex_to_str(n, num):
    map_row = ''
    while num:
        num, remainder = divmod(num, 2)
        if remainder == 0:
            map_row = ' ' + map_row
        else:
            map_row = '#' + map_row
    while len(map_row) < n:
        map_row = ' ' + map_row
    return map_row
  
