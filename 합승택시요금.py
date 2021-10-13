'''

플로이드 워셜 알고리즘을 이용하여 모든 노드에서 모든 노드까지의 경우의 수를 구해준다.

'''

def solution(n, s, a, b, fares):
    Inf = int(1e9)
    graph = [[Inf] * (n+1) for i in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0
    
    for i in fares:
        x, y, z = i[0], i[1], i[2]
        graph[x][y] = z
        graph[y][x] = z
    
    print(graph)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
    
    no_mid = graph[s][a] + graph[s][b]
    
    mid = {}
    for i in range(len(graph[s])):
        if i == 0 or i == s:
            continue
        else:
            mid[i] = graph[s][i] + graph[i][a] + graph[i][b]
    
    mid_min = min(mid.values())
    
    if no_mid >= mid_min:
        answer = mid_min
    else:
        answer = no_mid
    
    return answer
print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))