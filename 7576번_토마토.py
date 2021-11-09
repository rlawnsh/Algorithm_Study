'''
시간초과 예방:
1. 입력은 sys.stdin.readline()으로 받아주기
2. bfs문제 풀 때 시간초과 때문에 deque을 사용해서 풀어준다(popleft() 사용)

'''
import sys
from collections import deque

def bfs(data, tomato):
    len_t = len(tomato)
    answer = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    n_pop = 0
    while tomato:
        q = tomato.popleft()
        if q:
            n_pop += 1
        for i in range(4):
            if 0 <= q[0]+dx[i] < height and 0 <= q[1]+dy[i] < long:
                if data[q[0]+dx[i]][q[1]+dy[i]] == 0:
                    data[q[0]+dx[i]][q[1]+dy[i]] = 1
                    tomato.append([q[0]+dx[i], q[1]+dy[i]])
        if n_pop == len_t:
            answer += 1
            len_t = len(tomato)
            n_pop = 0
        
    return answer, data

long, height = map(int, sys.stdin.readline().split())

data = []
for i in range(height):
    data.append(list(map(int, sys.stdin.readline().split())))

tomato = deque([])
for i in range(height):
    for j in range(long):
        if data[i][j] == 1:
            tomato.append([i,j])
answer, data = bfs(data, tomato)

success = True
for i in data:
    if i.count(0) > 0:
        print(-1)
        success = False
        break

if success:
    print(answer-1)