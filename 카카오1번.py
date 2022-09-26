from collections import defaultdict
from copy import deepcopy
def solution(today, terms, privacies):
    answer = []
    today = list(map(int, today.split(".")))
    for_terms = defaultdict(list)
    for i in terms:
        today_ = deepcopy(today)
        term, month = map(str, i.split(" "))
        month = int(month)
        year = month // 12
        month = month % 12
        if today_[1] - month <= 0:
            year += 1
            month = today_[1] - month + 12
        else:
            month = today_[1] - month
        if today_[2] + 1 > 28:
            d = 1
            if month + 1 > 12:
                m = 1
                y = today_[0] - year + 1
            else:
                y = today_[0] - year
                m = month + 1
            for_terms[term].append([y,m,d])
        else:    
            for_terms[term].append([today_[0] - year, month, today_[2] + 1])
    for i in range(len(privacies)):
        case = list(map(str, privacies[i].split(" ")))
        case[0] = list(map(int, case[0].split(".")))
        temp = for_terms[case[1]][0]
        for j in range(len(temp)):
            if temp[j] > case[0][j]:
                answer.append(i+1)
                break
            if temp[j] < case[0][j]:
                break
    return answer
