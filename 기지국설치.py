def solution(n, stations, w):
    answer = 0

#     4 -> [3, 5]
    new_stations = []
    for i in stations:
        start = i-w
        end = i+w
        if start < 1:
            start = 1
        if end > n:
            end = n
        new_stations.append([start, end])
        
    check = []
#     1번째에 설치 안 될 경우
    if new_stations[0][0] != 1:
        check.append(new_stations[0][0])
            
    for i in range(len(new_stations) - 1):
        if new_stations[i+1][0] - new_stations[i][-1] - 1 > 0:
            check.append(new_stations[i+1][0] - new_stations[i][-1] - 1)

#     n번째에 설치 안 될 경우
    if new_stations[-1][-1] != n:
        check.append(n - new_stations[-1][-1])
        
    W = 2*w + 1  
    for i in check:
        answer += i//W
        if i % W > 0:
            answer += 1
    return answer