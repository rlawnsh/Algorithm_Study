n = int(input())
num = list(map(int, input().split()))
num.sort()
start = 0
end = len(num) - 1

case = []
while start < end:
    case.append([start, end, abs(num[start] + num[end])])
    if num[start] + num[end] < 0:
        start += 1
    elif num[start] + num[end] > 0:
        end -= 1
    else:
        print(num[start], end=" ")
        print(num[end])
        exit(0)

case.sort(key = lambda x:x[2])
print(num[case[0][0]], end=" ")
print(num[case[0][1]])