from collections import deque
import sys
input = sys.stdin.readline

def bfs(box, que):
    dx = [-1, 1, 0, 0, -1, 1]
    dy = [0, 0, -1, 1]
    while que:
        x, y, z = que.popleft() # [h, n, m]
        for i in range(6):
            if i == 4 or i == 5:
                a = x + dx[i]
                if 0<= a < h and box[a][y][z] == 0:
                    box[a][y][z] = box[x][y][z] + 1
                    que.append([a, y, z])
            else:
                b = y + dx[i]
                c = z + dy[i]
                if 0<= b < n and 0<= c < m and box[x][b][c] == 0:
                    box[x][b][c] = box[x][y][z] + 1
                    que.append([x, b, c])
    return box
m, n, h = map(int, input().split())
box = []
que = deque()
for i in range(h):
    temp = []
    for j in range(n):
        tomato = list(map(int, input().split()))
        for k in range(len(tomato)):
            if tomato[k] == 1:
                que.append([i,j,k])
        temp.append(tomato)
    box.append(temp)

box = bfs(box, que)
day = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                print(-1)
                exit(0)
            day = max(day, box[i][j][k])     

print(day-1)