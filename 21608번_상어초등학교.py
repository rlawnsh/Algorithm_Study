# from collections import defaultdict
# from copy import deepcopy
#
# def one(temp):
#     pos = []
#     for i in range(n):
#         for j in range(n):
#             if table[i][j] in temp:
#                 for k in range(4):
#                     x = i + dx[k]
#                     y = j + dy[k]
#                     if 0<= x <n and 0<= y <n and table[x][y] == 0:
#                         check = True
#                         for p in range(len(pos)):
#                             if [x,y] == pos[p][:2]:
#                                 pos[p][-1] += 1
#                                 check = False
#                         if check:
#                             pos.append([x, y, 1])
#     return pos
#
# def two(temp):
#     pos = []
#     if len(temp) == 0:
#         for i in range(n):
#             for j in range(n):
#                 if table[i][j] == 0:
#                     for k in range(4):
#                         x = i + dx[k]
#                         y = j + dy[k]
#                         if 0 <= x <n and 0<= y < n and table[x][y] == 0:
#                             check = True
#                             for p in range(len(pos)):
#                                 if [i,j] == pos[p][:2]:
#                                     pos[p][-1] += 1
#                                     check = False
#                             if check:
#                                 pos.append([i, j, 1])
#     else:
#         for i in range(n):
#             for j in range(n):
#                 if [i,j] in temp:
#                     for k in range(4):
#                         x = i + dx[k]
#                         y = j + dy[k]
#                         if 0 <= x <n and 0<= y < n and table[x][y] == 0:
#                             check = True
#                             for p in range(len(pos)):
#                                 if [i,j] == pos[p][:2]:
#                                     pos[p][-1] += 1
#                                     check = False
#                             if check:
#                                 pos.append([i, j, 1])
#                         elif 0 <= x < n and 0<= y < n and table[x][y] > 0:
#                             check = True
#                             for p in range(len(pos)):
#                                 if [i, j] == pos[p][:2]:
#                                     check = False
#                                     break
#                             if check:
#                                 pos.append([i, j, 0])
#
#     return pos
#
# n = int(input())
# case = []
# like = defaultdict(list)
# for i in range(n*n):
#     temp = list(map(int, input().split()))
#     case.append(temp)
#     like[temp[0]] = temp[1:]
#
# table = [[0]*n for _ in range(n)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# for i in case:
#     student = i[0]
#     for_one = i[1:]
#     res_one = one(for_one)
#     res_one.sort(key = lambda x:-x[2]) # [0, 1, 3] 0,1에 좋아하는 수 3
#     if len(res_one):
#         Max_res_one = res_one[0][-1]
#     for_two = []
#     for j in res_one:
#         if j[-1] == Max_res_one:
#             for_two.append(j[:2])
#         else:
#             break
#     if len(for_two) == 1:
#         x, y = for_two[0]
#         table[x][y] = student
#     else:
#         res_two = two(for_two)
#         res_two.sort(key = lambda x:-x[2])
#         if len(res_two):
#             Max_res_two = res_two[0][-1]
#         for_three = []
#         for k in res_two:
#             if k[-1] == Max_res_two:
#                 for_three.append(k[:2])
#             else:
#                 break
#
#         if len(for_three) == 1:
#             x, y = for_three[0]
#             table[x][y] = student
#         elif len(for_three) == 0:
#             three_escape = False
#             for i in range(n):
#                 for j in range(n):
#                     if table[i][j] == 0:
#                         table[i][j] = student
#                         three_escape = True
#                         break
#                 if three_escape:
#                     break
#         else:
#             for_three.sort(key= lambda x:(x[0], x[1]))
#             x, y = for_three[0]
#             table[x][y] = student
#
# answer = 0
# for i in range(n):
#     for j in range(n):
#         s = table[i][j]
#         cnt = 0
#         for k in range(4):
#             x = i + dx[k]
#             y = j + dy[k]
#             if 0 <= x < n and 0 <= y <n and table[x][y] in like[s]:
#                 cnt += 1
#         if cnt == 4:
#             answer += 1000
#         elif cnt == 3:
#             answer += 100
#         elif cnt == 2:
#             answer += 10
#         elif cnt == 1:
#             answer += 1
#
# # print(table)
#
# print(answer)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


n = int(input())
arr = [[0]*n for _ in range(n)]
## 한 번에 정보를 받음
students = [list(map(int, input().split())) for _ in range(n**2)]

## 학생 수 만큼 for문을 돌며 자리에 앉혀 줌.
for order in range(n**2):
    student = students[order]
    ## 여기다가 가능한 자리를 다 담아서 정렬 후 앉힘
    tmp = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < n and 0 <= nc < n:
                        if arr[nr][nc] in student[1:]:
                            like += 1
                        if arr[nr][nc] == 0:
                            blank += 1
                tmp.append([like, blank, i, j])
    ### !!!! like, blank는 클 수록, 행과 열의 수는 작을수록 답이니 lambda 뒤의 조건을 잘 줘야함!!!
    tmp.sort(key= lambda x:(-x[0], -x[1], x[2], x[3]))
    ### 정렬 후 젤 앞에 있는 리스트의 행과 열의 번호에 학생 앉히기
    arr[tmp[0][2]][tmp[0][3]] = student[0]

result = 0
## 점수를 매길 때는 학생 순서대로 점수 주기 위해 정렬함
students.sort()

for i in range(n):
    for j in range(n):
        ans = 0
        for k in range(4):
            nr, nc = i + dr[k], j + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] in students[arr[i][j]-1]:
                    ans += 1
        if ans != 0:
            result += 10 ** (ans-1)
print(result)