from collections import deque

n = int(input())
case = []
for i in range(n):
    case.append(list(map(int, input().split())))

dp = []
que = deque()

for i in range(n):
    for j in range(i, n):
        if case[j][0] + j <= n:
            que.append([case[j][0] + j, case[j][1]])
            while que:
                start = que.popleft()
                if start[0] == n:
                    dp.append(start[1])
                    continue
                for k in range(start[0], len(case)):
                    if k + case[k][0] <= n:
                        que.append([k + case[k][0], start[1] + case[k][1]])
                    else:
                        que.append([n, start[1]])

if dp:
    print(max(dp))
else:
    print(0)
