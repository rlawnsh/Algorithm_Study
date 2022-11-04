import math

def dfs(table, level, start):
    prime_check = True
    if len(start) > 0:
        if int(start) == 1:
            prime_check = False
        end = int(math.sqrt(int(start)))
        for i in range(2, end+1):
            if int(start) % i == 0:
                prime_check = False
                break
        
    if level == n:
        if prime_check:
            print(start)
        return

    if prime_check:        
        for i in range(len(table)):
            for j in table[i]:
                if visited[i] == False and i == level:
                    visited[i] = True
                    dfs(table, level+1, start + str(j))
                    visited[i] = False
                else:
                    break
    else:
        return


n = int(input())
table = []
table.append([i for i in range(1,10)])
table.extend([[i for i in range(10)] for _ in range(n-1)])
visited = [False] * n
level = 0
dfs(table, level, "")
