n,l,r = map(int,input().split())
popul = []
for _ in range(n):
    popul.append(list(map(int,input().split())))
dx = [-1,0,1,0]
dy = [0,-1,0,1]
#국경선을 열지말지 결정하는 함수
visitied = [[False]*n for _ in range(n)]
from collections import deque
def bfs(a,b,graph):
    queue = deque()
    queue.append((a,b))
    sump=graph[a][b]
    country = 1
    temp= [(a,b)]
    visitied[a][b] = True
    index = 0 #연합의 갯수
    #큐가 빌때까지 열수있는 국경선 열기
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0<=nx<n) and (0<=ny<n):
                if (not visitied[nx][ny]) and (l<=(abs(graph[nx][ny] - graph[x][y]))<=r):
                    queue.append((nx,ny))
                    visitied[nx][ny] = True
                    #국경선을 열수 있다면 연합에 국가를 추가
                    country+=1
                    sump+=graph[nx][ny]
                    temp.append((nx,ny))
    #큐가 비었다면 연합의 갯수 추가하기
    for i,j in temp:
        graph[i][j] = sump//country
    index+=1
    return index

ans = 0
while True:
    count = 0
    visitied = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visitied[i][j]:
                   count+=bfs(i,j,popul)
    if count == n*n:
        print(ans)
        break
    ans+=1