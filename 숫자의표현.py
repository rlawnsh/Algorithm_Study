'''

전형적인 완전 탐색 문제, for문을 돌려 1부터 n-1까지 탐색을 하고 내부 while문을 통해 
해당 숫자의 합이 나오면 answer값에 +1을 해주고 해당 숫자를 넘어 버리는 순간 break를 걸어 준다. 
그리고 마지막에 자기 숫자로 표현이 되므로(15=15) +1을 해주어 return한다.

'''

def solution(n):
    answer = 0
    for i in range(1,n):
        num = i
        for_num = num + 1
        while True:
            num += for_num
            for_num += 1
            if num == n:
                answer += 1
                break
            if num > n:
                break
    
    return answer+1