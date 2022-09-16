from copy import deepcopy
from itertools import combinations
from itertools import product
n, m = map(int, input().split())
office = []
for i in range(n):
    office.append(list(map(int, input().split())))

move = [[-1,0], [1,0], [0,-1], [0,1]]
move1 = list(combinations(move,1))
move2 = [([-1,0], [1,0]), ([0,-1], [0,1])]
move3 = [([-1,0], [0,-1]), ([-1,0], [0,1]), ([1,0], [0,-1]), ([1,0], [0,1])]
move4 = list(combinations(move,3))
print(move4)
move5 = list(combinations(move,4))

number = []
for i in range(len(office)):
    for j in range(len(office[i])):
        if office[i][j] != 0 and office[i][j] != 6:
            if office[i][j] == 1:
                number.append(move1)
            elif office[i][j] == 2:
                number.append(move2)
            elif office[i][j] == 3:
                number.append(move3)
            elif office[i][j] == 4:
                number.append(move4)
            elif office[i][j] == 5:
                number.append(move5)

all_way = list(product(*number))
case = []
for way in all_way:
    new_office = deepcopy(office)
    start = 0
    for i in range(len(new_office)):
        for j in range(len(new_office[i])):
            if new_office[i][j] != 0 and new_office[i][j] != 6 and new_office[i][j] != 7:
                for mv in way[start]:
                    x, y = mv[0], mv[1]
                    t_i, t_j = i, j
                    while 0<= t_i + x < n and 0<= t_j + y < m:
                        t_i += x
                        t_j += y
                        if new_office[t_i][t_j] == 6:
                            break
                        else:
                            new_office[t_i][t_j] = 7
                start += 1
    tmp = 0
    for i in range(len(new_office)):
        for j in range(len(new_office[i])):
            if new_office[i][j] == 0:
                tmp += 1
    case.append(tmp)

print(min(case))