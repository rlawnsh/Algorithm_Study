import copy
import sys
input = sys.stdin.readline

def dfs(backtrack, answer):
    pass

sentence = input()
n = int(input())

letter = []
for i in range(n):
    letter.append(input().rstrip())

data = []
backtrack = dict()

for i in letter:
    start = 0
    tmp = []
    cnt = 0
    end = len(i)
    while start <= len(sentence):
        part = sentence[start: end]
        find = True
        for j in range(len(i)):
            if i[j] in part:
                continue
            else:
                find = False
                break
        if find:
            for k in range(len(i)):
                if i[k] != part[k]:
                    cnt += 1
            tmp.append(start)
            backtrack[start] = []
            tmp.append(end)
            tmp.append(cnt)
            
            start += len(i)
            end += len(i)
        else:
            start += 1
            end += 1
    data.append(tmp)

answer = 0

for i in data:
    if len(i) > 3:
        for j in i[::3]:
            backtrack[j[0]].append(j)
    else:
        backtrack[i[0]].append(i)

dfs(backtrack, answer)


            


