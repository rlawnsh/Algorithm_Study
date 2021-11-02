# def solution(k, dungeons):
#     answer = 0
#     for i in range(len(dungeons)):
#         sub = dungeons[i][0] - dungeons[i][1]
#         dungeons[i].append(sub)
#     dungeons.sort(key= lambda x:-x[2])
    
#     for i in dungeons:
#         if k >= i[0]:
#             k -= i[1]
#             answer += 1
#     return answer

'''

순열을 이용하여 모든 경우의 수를 구해서 완전 탐색으로 풀 수 있다.

'''

from itertools import permutations
def solution(k, dungeons):
    all_dungeons = list(permutations(dungeons, len(dungeons)))
    arr = []
    
    for i in all_dungeons:
        new_k = k
        answer = 0
        for j in i:
            if new_k >= j[0]:
                new_k -= j[1]
                answer += 1
        arr.append(answer)
    
    answer = max(arr)
    return answer

print(solution(80,[[80,20],[50,40],[30,10]]))