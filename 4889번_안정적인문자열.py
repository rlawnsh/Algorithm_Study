import sys
input = sys.stdin.readline
from collections import deque

data = []

while True:
    data.append(deque(map(str, input().rstrip())))
    if "-" in data[-1]:
        data.pop()
        break

for i in range(len(data)):
    answer = 0
    open = 0
    close = 0
    temp = 0
    length = len(data[i])
    while data[i]:
        s = data[i].popleft()
        if s == "{":
            temp += 1
            open += 1
            if open > length // 2:
                answer += 1
                close += 1
                open -= 1
                temp -= 2
        else:
            temp -= 1
            if temp < 0:
                answer += 1
                open += 1
                temp += 2
            else:
                close += 1
    print("{0}. {1}".format(i+1, answer))
