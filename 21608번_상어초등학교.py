import sys
input = sys.stdin.readline
from collections import defaultdict

def one(temp):
    pos = []
    for i in range(n):
        for j in range(n):
            if table[i][j] in temp:
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0<= x <n and 0<= y <n and table[x][y] == 0:
                        check = True
                        for p in range(len(pos)):
                            if [x,y] == pos[p][:2]:
                                pos[p][-1] += 1
                                check = False
                        if check:
                            pos.append([x, y, 1])
    return pos

def two(temp):
    pos = []
    if len(temp) == 0:
        for i in range(n):
            for j in range(n):
                if table[i][j] == 0:
                    for k in range(4):
                        x = i + dx[k]
                        y = j + dy[k]
                        if 0 <= x <n and 0<= y < n and table[x][y] == 0:
                            check = True
                            for p in range(len(pos)):
                                if [i,j] == pos[p][:2]:
                                    pos[p][-1] += 1
                                    check = False
                            if check:
                                pos.append([i, j, 1])
    else:
        for i in range(n):
            for j in range(n):
                if [i,j] in temp:
                    for k in range(4):
                        x = i + dx[k]
                        y = j + dy[k]
                        if 0 <= x <n and 0<= y < n and table[x][y] == 0:
                            check = True
                            for p in range(len(pos)):
                                if [i,j] == pos[p][:2]:
                                    pos[p][-1] += 1
                                    check = False
                            if check:
                                pos.append([i, j, 1])
    return pos

n = int(input())
case = []
like = defaultdict(list)
for i in range(n*n):
    temp = list(map(int, input().split()))
    case.append(temp)
    like[temp[0]] = temp[1:]

table = [[0]*n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in case:
    student = i[0]
    for_one = i[1:]
    res_one = one(for_one)
    res_one.sort(key = lambda x:-x[2]) # [0, 1, 3] 0,1에 좋아하는 수 3
    if len(res_one):
        Max_res_one = res_one[0][-1]
    for_two = []
    for j in res_one:
        if j[-1] == Max_res_one:
            for_two.append(j[:2])
        else:
            break
    if len(for_two) == 1:
        x, y = for_two[0]
        table[x][y] = student
    else:
        res_two = two(for_two)
        res_two.sort(key = lambda x:-x[2])
        if len(res_two):
            Max_res_two = res_two[0][-1]
        for_three = []
        for k in res_two:
            if k[-1] == Max_res_two:
                for_three.append(k[:2])
            else:
                break

        if len(for_three) == 1:
            x, y = for_three[0]
            table[x][y] = student
        elif len(for_three) == 0:
            for i in range(n):
                for j in range(n):
                    if table[i][j] == 0:
                        table[i][j] = student
        else:
            for_three.sort(key= lambda x:(x[0], x[1]))
            x, y = for_three[0]
            table[x][y] = student

answer = 0
for i in range(n):
    for j in range(n):
        s = table[i][j]
        cnt = 0
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < n and 0 <= y <n and table[x][y] in like[s]:
                cnt += 1
        if cnt == 4:
            answer += 1000
        elif cnt == 3:
            answer += 100
        elif cnt == 2:
            answer += 10
        elif cnt == 1:
            answer += 1

print(answer)
