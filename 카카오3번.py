from itertools import product
def solution(users, emoticons):
    discount = [10, 20, 30, 40] 
    case = list(product(discount, repeat = len(emoticons)))
    answer = []
    for i in case: #(10,10,10,10)
        attend = 0
        start = 0
        for j in users: #[40,10000]
            temp = 0
            escape = False
            for k in range(len(i)):
                if j[0] <= i[k]:
                    temp += emoticons[k]*(100-i[k])//100
                    if temp >= j[1]:
                        escape = True
                        break
            if escape:
                attend += 1
            else:
                start += temp
        answer.append([attend, start])
    
    answer.sort(key = lambda x:(-x[0], -x[1]))
    return answer[0]