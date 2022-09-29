n = int(input())
arr = [[0] * 10 for i in range(1001)]
for i in range(10):
    arr[1][i] = 1

for i in range(2,1001):
    for j in range(10):
        if j == 0:
            arr[i][j] = sum(arr[i-1])
        else:
            arr[i][j] = arr[i][j-1] - arr[i-1][j-1]

print(sum(arr[n])%10007)