'''

모든 경우의 수를 구하면서 내려오는 방식으로 사이드는 그대로 계산을 하지만, 
중단은 경우의 수를 고려하여 max로 더 큰 값으로 결정을 짓는다. 

'''

def solution(triangle):
    for i in range(len(triangle)):
        for j in range(i+1):
            if i == 0 and j == 0:
                continue
            elif j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif i == j:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    answer = max(triangle[len(triangle)-1])
    return answer