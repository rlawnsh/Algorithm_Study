from collections import deque

def bfs(idx):
    que = deque()
    que.append(idx)
    visit = [False]*len(way)
    while que:
        q = que.popleft()
        for i in range(len(way)):
            if way[i][0] == q and visit[i] == False:
                visit[i] = True
                table[idx][way[i][1]] = 1
                que.append(way[i][1])

n = int(input())
table = [[0 for _ in range(n+1)] for _ in range(n+1)]
way = []
for i in range(n):
    way_i = [0] + list(map(int, input().split()))
    for j in range(len(way_i)):
        if way_i[j] == 1:
            way.append([i+1, j])

for i in range(1, n+1):
    bfs(i)

for i in range(1, n+1):
    print(" ".join(map(str, table[i][1:])))