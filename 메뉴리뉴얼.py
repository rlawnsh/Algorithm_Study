from collections import defaultdict
from itertools import combinations
def solution(orders, course):
    alpha = defaultdict(int)
    
    for i in orders:
        for j in i:
            alpha[j] += 1
    
    case = []
    for i in alpha:
        if alpha[i] >= 2:
            case.append(i)
    
    answer = defaultdict(list)
    for i in course: # 2
        temp = list(combinations(case, i)) 
        for j in temp: # ('A', 'B')
            ans = 0
            for k in orders: # "ABCFG"
                eacape = False
                for z in j: # A
                    if z in k:
                        escape = True
                    else:
                        escape = False
                        break
                if escape:
                    ans += 1
            if ans >= 2:
                answer[i].append([j, ans])
    result = []
    for i in answer:
        answer[i].sort(key = lambda x:-x[1])
        end = answer[i][0][1]
        for j in answer[i]:
            if end != j[1]:
                break
            t = list(j[0])
            t.sort()
            result.append(''.join(t))
    
    result.sort()
    return result