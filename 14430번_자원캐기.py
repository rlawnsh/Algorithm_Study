import sys
input = sys.stdin.readline

height, long = map(int, input().split())
data = []
for i in range(height):
    data.append(list(map(int, input().split())))

long_tmp = 0
for i in range(long):
    if data[0][i] > 0:
        data[0][i] += long_tmp
        long_tmp += 1
    else:
        data[0][i] += long_tmp

height_tmp = 0
for i in range(height):
    if data[i][0] > 0:
        data[i][0] += height_tmp
        height_tmp += 1
    else:
        data[i][0] += height_tmp

for i in range(1, height):
    for j in range(1, long):
        if data[i][j] == 0:
            data[i][j] = max(data[i-1][j], data[i][j-1])
        else:
            data[i][j] = max(data[i-1][j], data[i][j-1]) + 1
            
print(data[-1][-1])