def bs(mid, times, answer):
    for i in times:
        answer += mid//i
    return answer

def solution(n, times):
    end = 1e18
    start = 1
    while start <= end:
        mid = (start + end) // 2
        answer = 0
        ans = bs(mid, times, answer) 
        if ans < n:
            start = mid + 1
        elif ans >= n:
            end = mid - 1
    return start