def solution(n, s):
    answer = []
    if s // n == 0:
        answer.append(-1)
    else:
        temp = [s//n] * n
        left = s%n
        while left > 0:
            for i in range(len(temp)):
                temp[i] += 1
                left -= 1
                if left == 0:
                    break

        temp.sort()
        answer = temp
    
    return answer