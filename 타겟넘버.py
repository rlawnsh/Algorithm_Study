def solution(numbers, target):
    answer = 0
    data = []
    for i in range(2**len(numbers)):
        tmp = format(i, 'b')
        if len(tmp) != len(numbers):
            tmp = "0"*(len(numbers) - len(tmp)) + tmp
        data.append(tmp)
    
    for i in range(len(data)):
        tmp = 0
        data_pop = data.pop()
        for j in range(len(numbers)):
            idx = data_pop[j]
            if idx == "0":
                tmp += numbers[j]
            else:
                tmp -= numbers[j]
        if tmp == target:
            answer += 1
    return answer

###### 모범답안 1

from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

###### 모범답안 2

answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer

