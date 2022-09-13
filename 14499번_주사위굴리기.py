from collections import deque
n, m, x, y, k = map(int, input().split())
mapp = []
for i in range(n):
    tmp = list(map(int, input().split()))
    mapp.append(tmp)

order = list(map(int, input().split()))

width = deque([0,0,0,0])
height = deque([0,0,0])
for i in order:
    if i == 1:  
        if 0<= y + 1 <= m-1:
            y += 1 
            height.appendleft(width.pop())
            width.append(height.pop())
        else:
            continue
    elif i == 2:
        if 0 <= y - 1 <= m-1:
            y -= 1
            height.append(width.pop())
            width.append(height.popleft())
        else:
            continue
    elif i == 3:
        if 0 <= x - 1 <= n-1:
            x -= 1
            width.append(width.popleft())
        else:
            continue
    elif i == 4:
        if 0 < x + 1 <= n-1:
            x += 1
            width.appendleft(width.pop())
        else:
            continue

    if mapp[x][y] == 0:
        mapp[x][y] = width[-1]
    else:
        width[-1] = mapp[x][y]
        mapp[x][y] = 0
    if i == 4 or i == 3:
        height[1] = width[1]
    elif i == 1 or i == 2:
        width[1] = height[1]
    print(width[1])