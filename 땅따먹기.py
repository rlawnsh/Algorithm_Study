# 내 풀이

from copy import deepcopy

def solution(land):
    score = land[0]

    for i in land[1:]: # i = [5,6,7,8]
        score_copy = deepcopy(score)
        for j in range(4): 
            for k in range(4):
                if j == k:
                    continue
                else:
                    tmp = score_copy[j] + i[k]
                    if tmp >= score[k]:
                        score[k] = tmp
    
    answer = max(score)

    return answer

# 두 번째 풀이 - 깔끔한 DP

def solution(land):
    n = len(land)

    # dp[i][j] = i행 j열에서 점수의 최대값
    dp = [[0,0,0,0]] + land
    for i in range(1, n+1):
        dp[i][0] += max(dp[i-1][1], dp[i-1][2], dp[i-1][3])
        dp[i][1] += max(dp[i-1][0], dp[i-1][2], dp[i-1][3])
        dp[i][2] += max(dp[i-1][0], dp[i-1][1], dp[i-1][3])
        dp[i][3] += max(dp[i-1][0], dp[i-1][1], dp[i-1][2])

    return max(dp[n])



