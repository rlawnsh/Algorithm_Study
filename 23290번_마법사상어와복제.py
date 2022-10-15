from copy import deepcopy

def fmove():
    new_table = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4): # '555'
            if table[i][j] != 0:
                fish = list(table[i][j]) # ['5','5','5']
                for f in range(len(fish)): # fish[f] = '5'
                    for n in range(8):
                        dn = int(fish[f])
                        if dn - n <= 0:
                            dn = 8 + dn - n
                        else:
                            dn -= n
                        x, y = direct[str(dn)]
                        dx = i + x
                        dy = j + y
                        if  0 > dx or dx >= 4 or 0 > dy or dy >= 4 or smell[dx][dy] > 0 or [dx,dy] == [sx, sy]:
                            continue
                        else:
                            if new_table[dx][dy] == 0:
                                new_table[dx][dy] = str(dn)
                                fish[f] = ''
                            else:
                                new_table[dx][dy] += str(dn)
                                fish[f] = ''
                            break

                left_fish = "".join(fish)
                if len(left_fish) > 0:
                    if new_table[i][j] == 0:
                        new_table[i][j] = left_fish
                    else:
                        new_table[i][j] += left_fish
    return new_table

def smove():
    global sx, sy
    find_max = []
    for i in case:
        temp_table = deepcopy(table)
        init_sx, init_sy = sx, sy
        fish_cnt = 0
        possible = True
        for j in i:
            x, y = shark_direct[j]
            dx = init_sx + x
            dy = init_sy + y
            init_sx += x
            init_sy += y
            if 0 <= dx < 4 and 0 <= dy < 4:
                if temp_table[dx][dy] != 0:
                    fish_cnt += len(temp_table[dx][dy])
                    temp_table[dx][dy] = 0
            else:
                possible = False
                break
        if possible:
            ix, iy, iz = i
            temp = str(ix) + str(iy) + str(iz)
            find_max.append([temp, fish_cnt])

    find_max.sort(key= lambda x : (-x[1], x[0]))
    shark_move = list(map(int, find_max[0][0])) # [0, 0, 1]
    for i in shark_move:
        x, y = shark_direct[i]
        sx += x
        sy += y
        if table[sx][sy] != 0:
            table[sx][sy] = 0
            smell[sx][sy] = 3


m, s = map(int, input().split())
table = [[0 for _ in range(4)] for _ in range(4)]
smell = [[0 for _ in range(4)] for _ in range(4)]
for i in range(m):
    fx, fy, d = map(int, input().split())
    if table[fx-1][fy-1] != 0:
        table[fx-1][fy-1] += str(d)
    else:
        table[fx-1][fy-1] = str(d)

sx, sy = map(int, input().split())
sx -= 1
sy -= 1

direct = {'1': [0,-1], '2': [-1, -1], '3': [-1, 0], '4': [-1, 1], '5': [0, 1], '6': [1, 1], '7':[1, 0], '8': [1, -1]}
shark_direct = [[-1, 0], [0, -1], [1, 0], [0, 1]]
case = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            case.append([i, j, k])


for i in range(s):
    one = deepcopy(table)
    table = fmove()
    smove()
    for smell_x in range(4):
        for smell_y in range(4):
            if smell[smell_x][smell_y] > 0:
                smell[smell_x][smell_y] -= 1

    for copy_x in range(4):
        for copy_y in range(4):
            if one[copy_x][copy_y] != 0:
                if table[copy_x][copy_y] != 0:
                    table[copy_x][copy_y] += one[copy_x][copy_y]
                else:
                    table[copy_x][copy_y] = one[copy_x][copy_y]

answer = 0
for i in range(4):
    for j in range(4):
        if table[i][j] != 0:
            answer += len(table[i][j])

# for i in table:
#     print(i)
#
# for i in smell:
#     print(i)
# print([sx, sy])
print(answer)

