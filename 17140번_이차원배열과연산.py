from collections import defaultdict
def r_play(table):
    for i in range(len(table)):
        temp = defaultdict(int)
        for j in table[i]:
            if j == 0:
                continue
            else:
                temp[j] += 1
        res_temp = list(sorted(temp.items(), key=lambda x:(x[1], x[0]))) # [(2,1), (1,2)]
        new = []
        for rt in res_temp:
            new.extend(rt)
        table[i] = new
    return table
def c_play():
    temp = [[table[i][j] for i in range(len(table))] for j in range(len(table[0]))]
    temp = r_play(temp)
    temp = fill_zero(temp)
    temp = [[temp[i][j] for i in range(len(temp))] for j in range(len(temp[0]))]
    return temp

def fill_zero(table):
    max_column = max([len(i) for i in table])
    for i in range(len(table)):
        while len(table[i]) < max_column:
            table[i].append(0)
    return table

r, c, k = map(int, input().split())
r, c = r-1, c-1
table = []
for i in range(3):
    table.append(list(map(int, input().split())))

time = 0

while time <= 100:
    if 0<= r < len(table) and 0 <= c < len(table[0]):
        if table[r][c] == k:
            break
    time += 1
    row = len(table)
    column = len(table[0])

    if row >= column:
        table = r_play(table)
    else:
        table = c_play()
    table = fill_zero(table)
    if len(table) > 100:
        table = table[:100]
    if len(table[0]) > 100:
        for i in range(len(table)):
            table[i] = table[i][:100]

if time == 101:
    print(-1)
    exit(0)
print(time)
