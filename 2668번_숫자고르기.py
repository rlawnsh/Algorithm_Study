def dfs(start, temp):
    for i in range(len(number)):
        if number[i][0] == start and real_visit[i+1] == False:
            if visit[i]:
                return temp
            visit[i] = True
            temp.append(number[i][0])
            temp = dfs(number[i][1], temp)
            return temp
    return temp

n = int(input())
number = []
for i in range(n):
    second = int(input())
    number.append([i+1, second])

answer = []
real_visit = [False] * (n + 1)
for num in number:
    visit = [False] * n
    a, b = num
    res = dfs(b, [])
    if a in res:
        for i in res:
            real_visit[i] = True 
        answer.append(res)

result = []
for i in answer:
    for j in i:
        result.append(j)

result.sort()
print(len(result))
for i in result:
    print(i)

