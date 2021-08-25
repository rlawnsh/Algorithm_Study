'''

zip을 활용하여 두 배열을 합쳐 딕셔너리를 생성 할 수 있다. / sorted함수에서 람다를 사용하여 딕셔너리를 값 기준으로 정렬 할 수 있다.

'''

def solution(table, languages, preference):
    lp_dic = {name:value for name, value in zip(languages, preference)}
    t_dic = {}
    
    for i in table:
        ans = 0
        i = i.split(" ")
        for j in range(len(i)):
            if j == 0:
                continue
            else:
                temp = 6
                if i[j] in lp_dic:
                    ans += lp_dic[i[j]] * (temp - j)
        t_dic[i[0]] = ans
    
    t_dic = sorted(t_dic.items(), key= lambda item: item[1], reverse=True)
    M = t_dic[0][1]
    answer = t_dic[0][0]
    for i in t_dic:
        if M != i[1]:
            break
        else:
            if answer > i[0]:
                answer = i[0]

    return answer