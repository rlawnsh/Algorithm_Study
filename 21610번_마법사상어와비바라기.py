n, m = map(int, input().split())
table = []
for i in range(n):
    table.append(list(map(int, input().split())))

dx = [None, 0,-1,-1,-1,0,1,1,1]
dy = [None, -1,-1,0,1,1,1,0,-1]


cloud = [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]
for i in range(m):
    visited = [[True for i in range(n)] for j in range(n)]

    # 이동 처리
    move, cnt = map(int, input().split())
    mdx, mdy = dx[move] * cnt, dy[move] * cnt
    for c in range(len(cloud)):
        temp = cloud[c] # [0, 1]
        x, y = temp[0] + mdx, temp[1] + mdy
        if x < 0 or x >= n:
            x = x % n
        if y < 0 or y >= n:
            y = y % n
        cloud[c] = [x,y] # 이동 구름
        table[x][y] += 1

    for c in cloud:
        x, y = c[0], c[1]
        visited[x][y] = False
        for j in range(1, 5):
            j = j * 2
            wcx, wcy = x + dx[j], y +dy[j]
            if 0 <= wcx < n and 0<= wcy <n and table[wcx][wcy] > 0:
                table[x][y] += 1

    new_cloud = []
    for idx in range(n):
        for idy in range(n):
            if visited[idx][idy] and table[idx][idy] >= 2:
                new_cloud.append([idx, idy])
                table[idx][idy] -= 2

    cloud = new_cloud


answer = 0
for i in range(n):
    for j in range(n):
        answer += table[i][j]

print(answer)