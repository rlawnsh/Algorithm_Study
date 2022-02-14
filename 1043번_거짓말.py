import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy

n, m = map(int, input().split())

truth = deque(map(int, input().split()))
truth.popleft()

party = []
for i in range(m):
    temp = list(map(int, input().split()))
    temp.pop(0)
    party.append(temp)
    
while truth:
    q = truth.popleft()
    for i in range(len(party)):
        if q in party[i]:
            copy_ = deepcopy(party[i])
            for j in copy_:
                if q == j:
                    party[i].pop(party[i].index(q))
                else:
                    truth.append(j)

answer = 0
for i in party:
    if len(i) > 0:
        answer += 1

print(answer)
