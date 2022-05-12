def bfs(n, road, K):
    q = []
    copy_road = road.copy()
    for i in copy_road:
        if i[0] == 1 and i[2] <= K:
            n[i[1]] = min(i[2], n[i[1]])
            q.append([i[1], n[i[1]]])
            road.pop(road.index(i))
        elif i[1] == 1 and i[2] <= K:
            n[i[0]] = min(i[2], n[i[0]])
            q.append([i[0], n[i[0]]])
            road.pop(road.index(i))
    
    while q:
        q.sort(key=lambda x:x[1])    
        l_p = q.pop(0)
        copy_road = road.copy()
        for i in copy_road:
            if l_p[0] == i[0] and l_p[1] + i[2] <= K:
                n[i[1]] = min(l_p[1] + i[2], n[i[1]])
                q.append([i[1], n[i[1]]])
                road.pop(road.index(i))
            elif l_p[0] == i[1] and l_p[1] + i[2] <= K:
                n[i[0]] = min(l_p[1] + i[2], n[i[0]])
                q.append([i[0], n[i[0]]])
                road.pop(road.index(i))
    return n

def solution(N, road, K):
    answer = 0
    n = [500001 for i in range(N+1)]
    n = bfs(n, road, K)    
    
    for i in n:
        if i < 500001:
            answer += 1 

    return answer+1