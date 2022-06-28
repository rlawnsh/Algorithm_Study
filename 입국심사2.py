def solution(n, times):
    start = 1
    end =10**23
    
    while start < end:
        answer = 0
        mid = (start + end) //2
        for i in times:
            answer += mid//i
        if answer < n:
            start = mid + 1
        else:
            end = mid 
    
    return start