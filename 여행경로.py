from glob import escape

escape = False
def dfs(a, start, info, true):
    if len(true) == len(a):
        global escape
        escape = True
        info.append(start)
        return info
    
    for i in range(len(a)):
        if a[i][0] == start and i not in true:
            true.append(i)
            info.append(a[i][0])
            dfs(a, a[i][1], info, true)
            if escape:
                return info
            info.pop()
            true.pop()
    return info
def solution(tickets):
    answer = []
    tickets.sort(key = lambda x:(x[0],x[1]))
    info = []
    true = []
    answer = dfs(tickets, "ICN", info, true)
    return answer

print(solution([["ICN","JFK"],["JFK", "ICN"],["ICN", "HND"]]))

