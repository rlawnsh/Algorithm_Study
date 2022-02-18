# TODO 가장큰 점수를 마지막날에 처리하기, 그 날에 이미 스케줄이 있다면, 다음 앞날로 처리

import sys
input = sys.stdin.readline

num = int(input())
data = []

for i in range(num):
    data.append(list(map(int, input().split())))

data.sort(key= lambda x:-x[1])

answer = [0] * 1001

while data:
    tmp = data.pop(0)
    if answer[tmp[0]] == 0:
        answer[tmp[0]] = tmp[1]
    else:
        for i in range(tmp[0], 0, -1):
            if answer[i] == 0:
                answer[i] = tmp[1]
                break

print(sum(answer))