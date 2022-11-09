from collections import deque

def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    ms = []
    for i in timetable:
        ms.append(list(map(int,i.split(":"))))
    
    ms = deque(ms)
    start = [9,0]
    while n > 0:
        check = []
        person = m
        while person > 0 and ms:
            first = ms.popleft()
            if first[0] < start[0]:
                check.append(first)
            elif first[0] == start[0] and first[1] <= start[1]:
                check.append(first)
            else:
                ms.appendleft(first)
                break
            person -= 1
        
        if t == 60:
            start[0] += 1
        else:
            start[1] += t
            if start[1] >= 60:
                start[0] += 1
                start[1] += start[1] % 60
        n -= 1
    
    if m - len(check) == 0:
        temp = check[-1]
        a, b = temp[0], temp[1]-1
        if b < 0:
            a, b = str(a-1), str(60+b)
        else:
            a, b = str(a), str(b)
    else:
        a, b = start[0], start[1]
        if t == 60:
            a, b = str(a-1), str(b)
        else:
            b = b - t
            if b < 0:
                a, b = a-1, 60+b
        a,b = str(a), str(b)
        
    if len(a) == 1:
        a = "0" + a
    if len(b) == 1:
        b = "0" + b
    answer = a + ":" + b
        
    return answer