'''

import itertools를 한 뒤에 product를 활용하여 모든 조합을 찾은 뒤 데이터 처리를 해준다.

'''

import itertools
def solution(word):
    word = translate(word)
    word = tuple(word)
    
    result = list(itertools.product((["0","1","2","3","4","5"]), repeat=5))
    for_sub = []
    for i in range(len(result)):
        escape = False
        for j in range(len(result[i])):
            if result[i][j] == "0":
                for k in result[i][j+1:]:
                    if k != "0":
                        escape = True
                        break
            if escape:
                for_sub.append(result[i])
                break
    
    a_sub_b = [x for x in result if x not in for_sub]
    a_sub_b.sort()

    answer = a_sub_b.index(word)
    return answer

def translate(word):
    word = word.replace("A", "1")
    word = word.replace("E", "2")
    word = word.replace("I", "3")
    word = word.replace("O", "4")
    word = word.replace("U", "5")
    for_zero = 5 - len(word)
    word += "0"*for_zero
    
    return word

print(solution("AAAAE"))