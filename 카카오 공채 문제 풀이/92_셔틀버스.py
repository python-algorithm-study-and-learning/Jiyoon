def solution(n, t, m, timetable):
    timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    timetable.sort(reverse=True)
    
    answer = 0
    cur_time = 540    # "09:00"
    
    for _ in range(n):
        for _ in range(m):
            if timetable and timetable[-1] <= cur_time:
                answer = timetable.pop() - 1
            else:
                answer = cur_time
        
        cur_time += t
    
    hour, minute = divmod(answer, 60)
    answer = str(hour).zfill(2) + ":" + str(minute).zfill(2)
    return answer
    
