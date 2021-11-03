from itertools import combinations
from copy import deepcopy
def bfs(graph, virus_info, height, long):
    while virus_info:
        i = virus_info.pop(0)
        dx,dy = i[0], i[1]
        dx_u, dy_u = dx - 1, dy
        dx_d, dy_d = dx + 1, dy
        dx_l, dy_l = dx, dy - 1
        dx_r, dy_r = dx, dy + 1
        if 0<= dx_u <= height-1 and 0<= dy_u <= long-1 and graph[dx_u][dy_u] == 0:
            graph[dx_u][dy_u] = 2
            virus_info.append([dx_u,dy_u])
        if 0<= dx_d <= height-1 and 0<= dy_d <= long-1 and graph[dx_d][dy_d] == 0:
            graph[dx_d][dy_d] = 2
            virus_info.append([dx_d,dy_d])
        if 0<= dx_l <= height-1 and 0<= dy_l <= long-1 and graph[dx_l][dy_l] == 0:
            graph[dx_l][dy_l] = 2
            virus_info.append([dx_l,dy_l])
        if 0<= dx_r <= height-1 and 0<= dy_r <= long-1 and graph[dx_r][dy_r] == 0:
            graph[dx_r][dy_r] = 2
            virus_info.append([dx_r,dy_r])
    answer = 0
    for i in range(height):
        for j in range(long):
            if graph[i][j] == 0:
                answer += 1
    
    return answer
a, b = map(int, input().split())

arr = []
for i in range(a):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

place = []
virus = []
for i in range(a):
    for j in range(b):
        if arr[i][j] == 0:
            place.append([i,j])
        elif arr[i][j] == 2:
            virus.append([i,j])

block = list(combinations(place, 3))

place_able = []
for i in block:
    tmp_arr = deepcopy(arr)
    tmp_virus = deepcopy(virus)
    for j in i:
        tmp_arr[j[0]][j[1]] = 1
    place_able.append(bfs(tmp_arr,tmp_virus,a,b))

print(max(place_able))
