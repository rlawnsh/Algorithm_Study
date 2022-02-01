def solution(id_list, report, k):
    answer = []
    dict_id = dict()
    mail = dict()
    for i in id_list:
        dict_id[i] = 0
        mail[i] = set()
    
    for i in report:
        temp = list(i.split(" "))
        mail[temp[0]].add(temp[1])
    
    for i in mail:
        for j in mail[i]:
            dict_id[j] += 1
            
    stop = []
    for i in dict_id:
        if dict_id[i] >= k:
            stop.append(i)
    
    for i in mail:
        cnt = 0
        for j in mail[i]:
            if j in stop:
               cnt += 1
        answer.append(cnt)
    
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))

'''

모범 답안

'''

def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer