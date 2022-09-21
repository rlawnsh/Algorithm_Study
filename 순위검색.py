from itertools import combinations as combi
from collections import defaultdict


# 점수를 제외한 info 정보를 key값으로, 점수를 value값으로 해시맵 생성
def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list)
    for info in infos:
        info = info.split()
        info_key = info[:-1]
        info_val = int(info[-1])
        for i in range(5):
            for c in combi(info_key, i):  # 하나의 info에서 경우의 수 16개 만들기
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(info_val)  # 가능한 info 조합을 key, 점수를 value로 딕셔너리 저장
    for key in info_dict.keys():
        info_dict[key].sort()  # value값 점수들은 오름차순으로 정리

    for query in queries:
        query = query.split(' ')
        query_score = int(query[-1])
        query = query[:-1]

        for i in range(3):  # and 제거
            query.remove('and')
        while '-' in query:  # '-'제거
            query.remove('-')
        tmp_q = ''.join(query)

        # lower bound 사용해 query_score 보다 큰 점수들의 개수 구하기
        if tmp_q in info_dict:
            scores = info_dict[tmp_q]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start)
        else:
            answer.append(0)
    return answer