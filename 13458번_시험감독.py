n = int(input())
test = list(map(int, input().split()))
must, sub = map(int, input().split())

ans = 0

for t in test:
    to_sub = t - must
    ans += 1
    m = 0
    left = 0
    if to_sub > 0:
        m = to_sub // sub
        left = to_sub % sub
    ans += m
    if left:
        ans += 1

print(ans)