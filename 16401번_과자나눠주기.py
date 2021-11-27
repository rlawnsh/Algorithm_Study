import sys
input = sys.stdin.readline

M, N = map(int, input().split())
li = list(map(int, input().split()))
s, e = 1, max(li)
res = 0
while s <= e:
    m = (s+e)//2
    if sum([n//m for n in li]) >= M:
        res = m
        s = m+1
    else:
        e = m-1
print(res)
