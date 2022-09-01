import numpy as np
from itertools import combinations
from collections import deque

def solution(relation):
    answer = 0
    relation = deque(relation)
    # relation 같은 속성의 열이 있더라도 구별 해주기 위해 상단 행 추가
    relation.appendleft([i for i in range(len(relation[0]))])
    relation = np.transpose(relation)
    # 최소성을 위한 check list (학번이 들어갔으면 학번,이름 조합은 불가능)
    check = []
    for i in range(1, len(relation) + 1):
        case = list(combinations(relation, i))
        for j in case:              #[ryan, appeach], [music, math]
            find_dup = np.transpose(j)
            find_dup = list(map(tuple, find_dup))
            for_check = True
            if len(find_dup) == len(set(find_dup)):
                for k in check:
                    if set(k) & set(find_dup[0]) == set(k):
                        for_check = False
                if for_check:
                    answer += 1
                    check.append(find_dup[0])    
                    
    return answer


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))