n = int(input())
a = int(input())
apple = []
for i in range(a):
    x, y = map(int, input().split())
    apple.append([x - 1, y - 1])

direct = []  # 방향전환
d = int(input())
for i in range(d):
    x, y = map(str, input().split())
    direct.append([int(x), y])

board = [[False] * n for i in range(n)]
board[0][0] = True
for i in apple:
    x, y = i
    board[x][y] = 'apple'

up = [-1, 0]
down = [1, 0]
left = [0, -1]
right = [0, 1]

time = 0
now = right
head = [0, 0]
tail = [[0, 0]]
while True:

    head = [head[0] + now[0], head[1] + now[1]]
    hx, hy = head[0], head[1]
    tx, ty = tail[0][0], tail[0][1]

    # 중단
    if 0 > hx or hx >= n or 0 > hy or hy >= n or board[hx][hy] == True:
        break

    if board[hx][hy] != 'apple':
        board[tx][ty] = False
        board[hx][hy] = True
        tail.pop(0)
        tail.append([hx, hy])
    else:
        tail.append([hx,hy])
        board[hx][hy] = True

    time += 1

    for d in direct:  # [3, "D"]
        if time == d[0]:
            if now == right and d[1] == "D":
                now = down
            elif now == right and d[1] == "L":
                now = up
            elif now == up and d[1] == "D":
                now = right
            elif now == up and d[1] == "L":
                now = left
            elif now == down and d[1] == "D":
                now = left
            elif now == down and d[1] == "L":
                now = right
            elif now == left and d[1] == "D":
                now = up
            elif now == left and d[1] == "L":
                now = down

print(time + 1)