from collections import deque
from copy import copy

def check_zero(box):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 0:
                    return True
    return False

def bfs(box, que):
    dx = [-1, 1, 0, 0, -1, 1]
    dy = [0, 0, -1, 1]
    day = 0
    check = len(que)
    temp = 0
    while que:
        idx = que.popleft() # [h, n, m]
        check -= 1
        for i in range(6):
            s = copy(idx)
            if i == 4 or i == 5:
                if 0<= s[0] + dx[i] < h:
                    s[0] += dx[i]
                    if box[s[0]][s[1]][s[2]] == 0:
                        box[s[0]][s[1]][s[2]] = 1
                        temp += 1
                        que.append([s[0], s[1], s[2]])
            else:
                if 0<= s[1] + dx[i] < n and 0<= s[2] + dy[i] < m:
                    s[1] += dx[i]
                    s[2] += dy[i]
                    if box[s[0]][s[1]][s[2]] == 0:
                        box[s[0]][s[1]][s[2]] = 1
                        temp += 1
                        que.append([s[0], s[1], s[2]])
        if check == 0 and temp != 0:
            day += 1
            check = temp
            temp = 0

    if check_zero(box):
        return -1
    else:
        return day
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

print(bfs(box, que))
