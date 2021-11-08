num = int(input())
data = []
for i in range(num):
    data.append(int(input()))

dp = [0]
dp.append(1)
dp.append(2)
dp.append(4)
M = max(data)
start = 4
while start <= M:
    tmp = 0
    for i in range(start-3, start):
        tmp += dp[i]
    dp.append(tmp)
    start += 1

for i in range(len(data)):
    print(dp[data[i]])