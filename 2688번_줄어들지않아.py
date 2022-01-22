import sys
input = sys.stdin.readline

n = int(input())
num = []
for i in range(n):
    num.append(int(input()))

dp = [1] * 10
answer = [0,10]

M = max(num)
start = 2
while M >= start:
    dp_sum = sum(dp)
    tmp = []
    tmp.append(dp_sum)
    for i in range(len(dp)-1):
        tmp.append(tmp[i] - dp[i])
    
    answer.append(sum(tmp))
    dp = tmp
    start += 1
    
for i in num:
    print(answer[i])

