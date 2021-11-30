# import sys
# import heapq
# input = sys.stdin.readline

# num = int(input())
# for i in range(num):
#     dot = int(input())
#     data = list(map(int, input().split()))
#     heapq.heapify(data)
#     answer = 0
#     while len(data) > 2:
#         start = heapq.heappop(data)
#         for i in data:
#             end = 2 * i - start
#             if end in data:
#                 answer += 1
#     print(answer)


import sys
input = sys.stdin.readline

def bin_search(l,r,t):
    while l<=r:
        m = (l+r)//2
        if dots[m] == t:
            return 1
        if dots[m] > t:
            r = m-1
        else:
            l = m+1
    return 0

for _ in range(int(input().rstrip())):
    case = 0
    n = int(input().rstrip())
    dots = sorted(list(map(int, input().split())))
    l, r = 0, n-1
    
    for i in range(n-1):#점 a
        for j in range(i+1, n): #점 b
            dist = abs(dots[j]-dots[i])# 두 점 사이의 거리
            if bin_search(l, r, dots[j] + dist):#target은 두점사이 거리만큼 떨어진 다른 점
                case+=1
    print(case)