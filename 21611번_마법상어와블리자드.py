# import sys
# input = sys.stdin.readline
# from collections import deque
#
# def copy_move():
#     temp = []
#     for i in move:
#         temp = deque([m[:] for m in move])
#     return temp
#
# def destroy():
#     for i in range(1, s+1):
#         x, y = shark_s + direct[d][0]*i, shark_y + direct[d][1]*i
#         table[x][y] = 0
#
# def check():
#     check_move = copy_move()
#     blank = deque()
#     while check_move:
#         x, y = check_move.popleft()
#         if table[x][y] == 0:
#             blank.append([x,y])
#         else:
#             if len(blank) > 0:
#                 bx, by = blank.popleft()
#                 if table[x][y] == 0:
#                     break
#                 table[bx][by] = table[x][y]
#                 table[x][y] = 0
#                 blank.append([x,y])
#
# def explode():
#     while True:
#         explode_move = copy_move()
#         duplicate = deque()
#         escape = True
#
#         while explode_move:
#             x, y = explode_move.popleft()
#             if duplicate:
#                 dup_x, dup_y = duplicate[-1]
#                 if table[dup_x][dup_y] == table[x][y] and table[x][y] != 0:
#                     duplicate.append([x,y])
#                 else:
#                     if len(duplicate) >= 4:
#                         escape = False
#                         dup_x, dup_y = duplicate[0]
#                         check_explode[table[dup_x][dup_y]] += len(duplicate)
#                         while duplicate:
#                             dup_x, dup_y = duplicate.popleft()
#                             table[dup_x][dup_y] = 0
#                     else:
#                         duplicate.clear()
#
#                     duplicate.append([x,y])
#             else:
#                 duplicate.append([x,y])
#         check()
#         if escape:
#             break
#
# def change():
#     change_move = copy_move()
#     change_table = [[0 for _ in range(n)] for _ in range(n)]
#     change_table_move = copy_move()
#     change_que = deque()
#     while change_move:
#         c_x, c_y = change_move.popleft()
#         if table[c_x][c_y] == 0:
#             break
#         if change_que:
#             x, y = change_que[-1]
#             if table[x][y] == table[c_x][c_y]:
#                 change_que.append([c_x, c_y])
#             else:
#                 for ctm in range(2):
#                     if len(change_table_move) == 0:
#                         continue
#                     ctm_x, ctm_y = change_table_move.popleft()
#                     if ctm == 0:
#                         change_table[ctm_x][ctm_y] = len(change_que)
#                     else:
#                         t_x, t_y = change_que[-1]
#                         change_table[ctm_x][ctm_y] = table[t_x][t_y]
#                 change_que.clear()
#                 change_que.append([c_x, c_y])
#         else:
#             change_que.append([c_x, c_y])
#
#     return change_table
#
# n, m = map(int, input().split())
# table = []
# for _ in range(n):
#     table.append(list(map(int, input().split())))
#
# magic = [] # [[2,2]]
# for _ in range(m):
#     magic.append(list(map(int, input().split())))
#
# direct = [0, [-1, 0], [1, 0], [0,-1], [0,1]]
# shark_s, shark_y = n//2, n//2
#
# move = deque()
# mx = shark_s
# my = shark_y
# start = 1
# while 0<= mx <n and 0<= my-1 <n:
#     cnt = start
#     temp = deque()
#     my -= 1
#     move.append([mx, my])
#     for i in range(cnt):
#         mx += direct[2][0]
#         my += direct[2][1]
#         move.append([mx, my])
#
#     for _ in range(cnt+1):
#         mx += direct[4][0]
#         my += direct[4][1]
#         move.append([mx, my])
#
#     for _ in range(cnt+1):
#         mx += direct[1][0]
#         my += direct[1][1]
#         move.append([mx, my])
#
#     for _ in range(cnt+1):
#         mx += direct[3][0]
#         my += direct[3][1]
#         move.append([mx, my])
#
#     start += 2
#
#
# check_explode = {1:0, 2:0, 3:0}
# for i in magic:
#     d, s = i
#     destroy()
#     check()
#     explode()
#     table = change()
#
# answer = 0
# for i in check_explode:
#     if i == 1:
#         answer += check_explode[i]
#     elif i == 2:
#         answer += check_explode[i] * 2
#     else:
#         answer += check_explode[i] * 3
#
# print(answer)
#

N, M = map(int, input().split())
board = [[] for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))
blizard = [[] for _ in range(M)]
for i in range(M):
    blizard[i] = list(map(int, input().split()))
shark = [(N - 1) // 2, (N - 1) // 2]
result = [0, 0, 0]


def destroy(d, s):
    global board, N, shark

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(1, s + 1):
        nx = shark[0] + dx[d - 1] * i
        ny = shark[1] + dy[d - 1] * i

        # 격자를 넘어가면 continue
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            break

        # 파괴
        board[nx][ny] = 0


def board2list():
    global board

    arr = []
    cur = shark[:]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    num = 1
    direction = 0
    is_over = False
    while not is_over:
        for i in range(2):
            for j in range(num):
                cur[0] += dx[direction]
                cur[1] += dy[direction]

                # 격자 밖으로 넘어간다면
                if cur[0] < 0 or cur[1] < 0 or cur[0] >= N or cur[1] >= N:
                    is_over = True
                    break

                # 회오리 순서대로 배열에 append
                arr.append(board[cur[0]][cur[1]])
            direction = (direction + 1) % 4
            if is_over:
                break
        num += 1

    return arr


def move(arr):
    # 구슬 배열에서 빈칸 제거
    return [arr[i] for i in range(len(arr)) if arr[i] != 0]


def explode(arr):
    global result

    # 구슬이 존재하지 않는 경우
    if not arr:
        return [], False

    # 연속하는 구슬이 4개 이상이면 폭발
    cur_marble = arr[0]
    cur_num = 1
    is_removed = False

    for i in range(1, len(arr)):
        # 같은 색의 구슬이라면
        if arr[i] == cur_marble:
            cur_num += 1
        else:
            # 다른 색의 구슬인데 4개 미만인 경우
            if cur_num < 4:
                cur_num = 1
                cur_marble = arr[i]
            # 다른 색의 구슬인데 4개 이상인 경우
            else:
                # 개수만큼 이전 구슬들 폭발
                for j in range(1, cur_num + 1):
                    arr[i - j] = 0
                # result에 폭발 개수 저장
                result[cur_marble - 1] += cur_num
                is_removed = True
                # 새로운 색으로 update
                cur_num = 1
                cur_marble = arr[i]
    # 마지막으로 현재 구슬들 체크
    if cur_num >= 4:
        is_removed = True
        for j in range(1, cur_num + 1):
            arr[len(arr) - j] = 0
        result[cur_marble - 1] += cur_num

    return arr, is_removed


def make_group(arr):
    # 구슬이 존재하지 않는 경우
    if not arr:
        return []

    # 그룹으로 묶어서 [구슬 개수, 구슬 번호]로 변경
    new_arr = []
    cur_type = arr[0]
    cur_num = 1

    for i in range(1, len(arr)):
        # 같은 색의 구슬인 경우
        if arr[i] == cur_type:
            cur_num += 1
        else:
            # 다른 색의 구슬인 경우 그룹 [구슬 개수, 구슬 번호] 추가
            new_arr.append(cur_num)
            new_arr.append(cur_type)
            cur_num = 1
            cur_type = arr[i]
    # 마지막 그룹 체크
    new_arr.append(cur_num)
    new_arr.append(cur_type)

    return new_arr


def list2board(arr):
    global N, shark

    # list 를 회오리 모양 보드로 변경
    new_board = [[0 for _ in range(N)] for _ in range(N)]

    # 구슬이 없다면
    if not arr:
        return new_board

    cur = shark[:]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    num = 1
    direction = 0
    cur_arr = 0
    is_over = False
    while not is_over:
        for i in range(2):
            for j in range(num):
                cur[0] += dx[direction]
                cur[1] += dy[direction]

                # 격자 밖으로 넘어간다면
                if cur[0] < 0 or cur[1] < 0 or cur[0] >= N or cur[1] >= N:
                    is_over = True
                    break

                # 회오리 순서대로 보드에 append
                new_board[cur[0]][cur[1]] = arr[cur_arr]
                cur_arr += 1
                # 구슬이 더이상 없다면
                if cur_arr >= len(arr):
                    is_over = True
                    break
            if is_over:
                break
            direction = (direction + 1) % 4
        num += 1

    return new_board


def solution():
    global M, blizard, board, result

    for i in range(M):
        destroy(blizard[i][0], blizard[i][1])  # 방향, 거리
        arr = board2list()
        arr = move(arr)
        while arr:
            arr, is_removed = explode(arr)
            if not is_removed:
                break
            arr = move(arr)
        board = list2board(make_group(arr))

    print(result[0] + 2 * result[1] + 3 * result[2])


solution()