from collections import deque
def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    B = deque(B)
    answer = 0
    
    for i in range(len(A)):
        if A[i] < B[i]:
            answer += 1
        else:
            B.appendleft(B.pop())
    return answer