from itertools import permutations
from copy import deepcopy
def solution(expression):
    sign = []
    for i in expression:
        if i == "+" or i == "*" or i == "-":
            sign.append(i)
    number = expression.replace("+", " ").replace("*", " ").replace("-", " ").split()
    number = list(map(int, number))

    set_sign = set(sign)
    set_sign = list(permutations(set_sign, len(set_sign)))
    
    result = []
    for i in set_sign: # [-,*,+]
        copy_number = deepcopy(number)
        copy_sign = deepcopy(sign)
        for j in i: # -
            k = 0
            while j in copy_sign: # [-, *, -, +]
                if copy_sign[k] == j:
                    if j == "-":
                        copy_number[k] -= copy_number[k+1]
                    elif j == "*":
                        copy_number[k] *= copy_number[k+1]
                    else:
                        copy_number[k] += copy_number[k+1]
                    copy_number.pop(k+1)
                    copy_sign.pop(k)
                    k = 0
                    continue
                k += 1
        result.append(abs(copy_number[0]))

    
    answer = max(result)
    return answer

print(solution("100-200*300-500+20"))