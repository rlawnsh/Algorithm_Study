'''

소수 판정 알고리즘을 외워야 하나?

'''

from collections import deque
import math

def find_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False

    return True

def solution(n, k):
    answer = 0
    n_k = deque()
    while n >= 1:
        n_k.appendleft(str(n % k))
        n = n // k

    n_k = "".join(n_k)
    num = list(n_k.split("0"))

    for i in num:
        if len(i) > 0:
            TF = find_prime(int(i))
            if TF:
                answer += 1

    return answer