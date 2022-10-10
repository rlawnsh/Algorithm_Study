from collections import deque
def bfs(maps, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * m for i in range(n)]
    que = deque()
    que.append([0,0])
    visited[0][0] = True
    while que:
        a, b = que.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m and maps[x][y] == 1 and visited[x][y] == False:
                maps[x][y] = maps[a][b] + 1
                que.append([x,y])
                visited[x][y] = True
    return maps
def solution(maps):
    answer = 0
    result = bfs(maps, len(maps), len(maps[0]))
    if result[-1][-1] == 1:
        answer = -1
    else:
        answer = result[-1][-1]
    return answer