from datetime import datetime, timedelta
import re

def solution(lines):
    time_logs = []
    for line in lines:
        second = float(line.split(' ')[2].split('s')[0]) - 0.001
        match = re.match(r'^([\d-]+ [\d:.]+)', line)
        end = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S.%f')
        start = end - timedelta(seconds=second)
        time_logs.append((start, end))
        
    answer = 1
    for i, times in enumerate(time_logs):
        cur = times[1]
        cur_plus_one = cur + timedelta(seconds=0.999)
        
        cnt = 1
        for start, end in time_logs[i + 1:]:
            if (start <= cur_plus_one <= end) or (cur <= end <= cur_plus_one):
                cnt += 1 
        answer = max(answer, cnt)
        
    return answer
    
