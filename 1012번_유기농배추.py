import sys
sys.setrecursionlimit(10**5) #### 재귀 깊이 늘리기
def dfs(data, x, y, long, height):
    if data[x][y] == 0:
        return
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        data[x][y] = 0
        if 0 <= x + dx[i] < height and 0 <= y + dy[i] < long and data[x+dx[i]][y+dy[i]] == 1:
            dfs(data, x + dx[i], y + dy[i], long, height)

case = int(input())
arr_answer = []
for i in range(case):
    long, height, num = map(int, input().split())
    answer = 0
    data = [[0]*long for i in range(height)]
    for j in range(num):
        a, b = map(int, input().split())
        data[b][a] = 1
    for x in range(height):
        for y in range(long):
            if data[x][y] == 1: 
                dfs(data, x, y, long, height)
                answer += 1

    arr_answer.append(answer)

for i in arr_answer:
    print(i)