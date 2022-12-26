n, k = map(int, input().split())
number = list(map(int, input().split()))
case = []
ryan_cnt = 0
if number.count(1) < k:
    print(-1)
    exit(0)
for i in range(len(number)):
    if number[i] == 1:
        start, end = i, i
        break
idx = 0
ryan_cnt_case = []
while end < n:
    if number[end] == 1:
        case.append(end)
        ryan_cnt += 1
    if ryan_cnt == k:
        ryan_cnt_case.append(end-start+1)
        if len(case) > 1:
            idx += 1
        start = case[idx]
        ryan_cnt -= 1

    end += 1
print(min(ryan_cnt_case))