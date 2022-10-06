from itertools import combinations
n = int(input())
num = [i for i in range(10)]
case = []

for i in range(1, 11):
    for j in combinations(num, i):
        j = list(j)
        j.sort(reverse=True)
        j = map(str, j)
        j = "".join(j)
        case.append(int(j))

case.sort()
if n > len(case) - 1:
    print(-1)
    exit(0)
print(case[n])