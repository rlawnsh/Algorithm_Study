import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    q.append(start)
    while q:
        tmp = q.popleft()
        for i in range(4):
            if 0 <= tmp[0] + dx[i] < height and 0 <= tmp[1] + dy[i] < long:
                if data[tmp[0]+dx[i]][tmp[1]+dy[i]] == 0:
                    data[tmp[0]+dx[i]][tmp[1]+dy[i]] = 2
                    q.append([tmp[0]+dx[i], tmp[1]+dy[i]])
    

height, long = map(int, input().split())
data = []
for i in range(height):
    data.append(list(map(str, input().split())))

for i in range(height):
    data[i] = list(map(int,list(data[i][0])))

for j in range(long):
    if data[0][j] == 0:
        data[0][j] = 2
        start  = [0,j]
        bfs(start)

if 2 in data[-1]:
    print("YES")
else:
    print("NO")