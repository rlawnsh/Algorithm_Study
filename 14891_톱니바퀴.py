import sys
from collections import deque
input = sys.stdin.readline

def rotate(arr, direct): # 1 -1 x x , 도는방향
    if direct == "x":
        return arr

    new_arr = deque()
    if direct == 1:
        new_arr.append(arr.pop())
        for i in arr:
            new_arr.append(i)
    else:
        pl = arr.popleft()
        for i in arr:
            new_arr.append(i)
        new_arr.append(pl)
    return new_arr

def ns(temp, data, init): # 순차적으로 2,6번 째 index 검사 0,1 / 1,2 / 2,3
    for i in range(init, 3):
        if data[i][2] != data[i+1][6]:
            temp.append(-temp[i])
        else:
            temp.append("x")
            while len(temp) < 4:
                temp.append("x")
            return temp
    return temp

def checking(data): # rotation = [[1, -1, x, x], ... ]
    rotation = []
    temp = [1]
    temp = ns(temp, data, 0)

    rotation.append(temp) # 1 -1 x x
    for i in range(1,4):
        new_temp = []
        if temp[i] != "x":
            for j in temp:
                if j == "x":
                    new_temp.append("x")
                else:
                    new_temp.append(-j)
        else:
            for k in range(i):
                new_temp.append("x")
            new_temp.append(1)
            new_temp = ns(new_temp, data, i)
        rotation.append(new_temp)
        temp = new_temp

    return rotation

data = deque()

for i in range(4):
    data.append(deque(map(int, input().rstrip())))
k = int(input())

what = [] # [ [2,-1], [0,1] ]
for i in range(k):
    what.append(list(map(int, input().split())))
    what[i][0] -= 1

start = 0

while start < 1:
    for i in what:
        rotation = checking(data)
        # print(rotation)
        for j in range(len(rotation[i[0]])): # 1 -1 x x
            if i[1] == -1:
                if rotation[i[0]][j] != "x":
                    rotation[i[0]][j] *= -1
            
            data[j] = rotate(data[j], rotation[i[0]][j])
    start += 1
                
answer = 0
for i in range(len(data)):
    if data[i][0] == 1:
        answer += 2**i
print(answer)