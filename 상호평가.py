'''

scores를 numpy의 transpose를 활용하여 전치행렬로 만들어 준다.

'''

import copy
import numpy as np

def solution(scores):
    scores = np.transpose(scores)
    answer = ''
    mean = []
    n = 0

    for i in scores:
        score = 0
        high_low = False
        copy_i = copy.deepcopy(i)
        for j in range(len(i)):
            if j == n:
                check = copy_i[j]
                if copy_i[j] == max(copy_i) or copy_i[j] == min(copy_i):
                    copy_i = np.delete(copy_i, j)
                    if check == max(copy_i) or check == min(copy_i):
                        high_low = False
                    else:
                        high_low = True
                        continue
            score += scores[n][j]
            
        if high_low:
            mean.append(score/(len(i)-1))
        else:
            mean.append(score/len(i))
        n += 1
    
    for i in mean:
        if 90 <= i:
            answer += "A"
        elif 80 <= i < 90:
            answer += "B"
        elif 70 <= i < 80:
            answer += "C"
        elif 50 <= i < 70:
            answer += "D"
        else:
            answer += "F"
            
    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))