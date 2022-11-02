from itertools import combinations

def dfs(start, case):
    # (2, 4)
    visit = table[start]
    for i in visit:
        if visited[i] == False and i in case:
            visited[i] = True
            dfs(i, case)

n = int(input())
people = list(map(int, input().split()))
num = [i for i in range(1, n+1)]
table = [0]
for i in range(n):
    temp = list(map(int, input().split()))
    table.append(temp[1:])

# {1: 5, 2: 2, ...}
number = dict() 
for i in range(len(people)):
    number[i+1] = people[i]

diff = []
for i in range(1, n//2 + 1):
    case1 = list(combinations(num, i))
    for c1 in case1:
        case2 = []
        for j in num:
            if j not in c1:
                case2.append(j)

        case1_people = 0
        case2_people = 0
        visited = [False] * (n + 1)
        visited[c1[0]] = True
        dfs(c1[0], c1)
        case1_res = True
        for i in c1:
            if visited[i] == False:
                case1_res = False
                break
        
        case2_res = True
        visited = [False] * (n + 1)
        visited[case2[0]] = True
        dfs(case2[0], case2)
        for i in case2:
            if visited[i] == False:
                case2_res= False
                break

        if case1_res and case2_res:
            for i in c1:
                case1_people += number[i]
            for i in case2:
                case2_people += number[i]

        if case1_people != 0 and case2_people != 0:
            diff.append(abs(case1_people - case2_people))

if len(diff) == 0:
    print(-1)
else:
    print(min(diff))
