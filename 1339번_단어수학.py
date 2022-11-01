from collections import deque
from collections import defaultdict

n = int(input())
table = []
for i in range(n):
    temp = deque(input())
    for j in range(8 - len(temp)):
        temp.appendleft('0')
    table.append(temp)

alpha = defaultdict(int)
cnt = 90000000
for i in range(8):
    for j in range(len(table)):
        if table[j][i] != '0':
            alpha[table[j][i]] += cnt
    cnt /= 10
    cnt -= 1

alpha_sort = list(sorted(alpha.items(), key = lambda x:-x[1]))

alpha_number = dict()
number = 9
for i in alpha_sort:
    alpha_number[i[0]] = number
    number -= 1

answer = 0
for i in range(len(table)):
    for j in range(8):
        if table[i][j] != '0':
            table[i][j] = str(alpha_number[table[i][j]])
    answer += int(''.join(table[i]))

print(answer)