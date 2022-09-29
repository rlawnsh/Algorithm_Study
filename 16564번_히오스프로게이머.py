from copy import copy
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
level = []
for i in range(n):
    level.append(int(input()))

max_level = min(level) + 1e9
min_level = min(level)

while min_level <= max_level:
    mid = int((max_level + min_level) // 2)
    copy_k = copy(k)
    big_then_mid = 0
    for i in level:
        if i >= mid:
            big_then_mid += 1
            continue
        copy_k -= (mid - i)
        if copy_k < 0:
            max_level = mid - 1
            break
    if copy_k >= len(level) - big_then_mid:
        min_level = mid + 1
    elif 0 <= copy_k < len(level):
        break

print(mid)
