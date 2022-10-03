n, k = map(int, input().split())

table = [[0] * 201 for _ in range(201)]
for i in range(201):
    table[1][i] = i
    
for i in range(2,201):
    for j in range(201):
        if j == 0:
            table[i][j] = 0
        else:
            table[i][j] = table[i-1][j] + table[i][j-1]

print(table[n][k]%int(1e9))
