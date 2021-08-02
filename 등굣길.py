'''

전형적인 DP 문제, 이차원 배열 arr을 만들어 puddles에 속한 값들은 모두 0으로 하고, arr[0][:m]과 arr[:n][0]을 웅덩이가 나오기 전까지는 1 그 이후로는 모두 0으로 설정한다. 
그 다음 배열을 채워주면 되는데, 이중 for문을 활용하여 이차원 배열의 값을 arr[i][j] = arr[i-1][j] + arr[i][j-1]로 채워 주면 된다.

'''

def solution(m, n, puddles):
    arr = [[None for col in range(m)] for row in range(n)]

    for i in puddles:
        arr[i[1]-1][i[0]-1] = 0
    
    for i in range(1,m):
        if arr[0][i] == 0:
            if i < m-1:
                arr[0][i+1] = 0
        else:
            arr[0][i] = 1
    
    for i in range(1,n):
        if arr[i][0] == 0:
            if i < n-1:
                arr[i+1][0] = 0
        else:
            arr[i][0] = 1
    
    for i in range(1,n):
        for j in range(1,m):
            if arr[i][j] == 0:
                continue
            else:
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
                
            
    return arr[n-1][m-1] % 1000000007

print(solution(4,3,[[2,2],[2,1]]))