# 패널티 - 처음 맞았습니다를 받은시간 + (제출횟수-1) * 20 분단위
import sys
import copy

def update(dict):
    dict = sorted(dict.items(), key=lambda x:(-x[1][0], x[1][1], x[1][2]))
    return dict

data = list(map(int, sys.stdin.readline().split()))
time = []
for i in range(data[1]):
    time.append(list(map(str, sys.stdin.readline().split())))

for i in range(len(time)):
    for j in range(len(time[i])):
        if j == 0:
            temp = time[i][j].split(":")
            time[i][0] = (int(temp[0])*60)+int(temp[1])
        else:
            time[i][j] = int(time[i][j])

# 참가자번호: 총점, 패널티, 마지막 정답시간
record = {}
for i in range(1,data[0]+1):
    record[i] = [0,0,0]

for i in range(len(time)):
    if time[i][0] > 180:
        idx = i
        break
    record[time[i][1]][0] += 1
    record[time[i][1]][1] += time[i][0] + (time[i][3]-1)*20
    record[time[i][1]][2] = time[i][0]

record = update(record)
for i in range(len(record)):
    record[i] = list(record[i])
    record[i].append(0)

after_3 = time[idx:]
after_3.sort(key=lambda x:x[2])

w = len(after_3)
while w > 0:
    for i in range(len(record)-1, -1,-1):
        escape = False
        for j in range(len(after_3)):
            if record[i][0] == after_3[j][1]:
                역전 = record[i][0]
                record[i][1][0] += 1
                record[i][1][1] += after_3[j][0] + (after_3[j][3]-1)*20
                record[i][1][2] = after_3[j][0]
                after_3.pop(j)
                escape = True
                break
        if escape:
            break
    temp = copy.deepcopy(record)
    record.sort(key=lambda x:(-x[1][0], x[1][1], x[1][2]))
    if temp != record:
        for i in range(len(record)):
            if record[i][0] == 역전:
                record[i][2] += 1
    w -= 1

record.sort(key=lambda x:(-x[2],-x[1][0],x[1][1],x[1][2]))
print(record[0][2])





    
