def solution(m, n, puddles):
    answer = 0
    table = [[-1 for i in range(m)] for i in range(n)]
    for i in puddles:
        table[i[1]-1][i[0]-1] = 0
        
    for i in range(m):
        if table[0][i] == 0:
            for j in range(i, m):
                table[0][j] = 0
            break
        else:
            table[0][i] = 1
            
    for i in range(n):
        if table[i][0] == 0:
            for j in range(i, n):
                table[j][0] = 0
            break
        else:
            table[i][0] = 1
            
    for i in range(1, n):
        for j in range(1, m):
            if table[i][j] == 0:
                continue
            else:
                table[i][j] = table[i-1][j] + table[i][j-1]
    
    answer = table[n-1][m-1]
    return answer % 1000000007