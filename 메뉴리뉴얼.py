from itertools import combinations
def solution(orders, course):
    answer = []
    new_orders = []
    for i in orders:
        tmp = list(i)
        tmp.sort()
        new_orders.append(tmp)
    
    max_orders = len(max(orders,key = lambda x:len(x)))
    for num in course:
        if max_orders < num:
            continue
        ex = []
        for i in new_orders:
            ex.extend(list(combinations(i, num)))
        cnt_dict = {}
        result = []
        for num_ex in ex: # (A, B)
            cnt = 0
            for order in new_orders: # [A,B,C,F,G]
                for_cnt = True
                for j in num_ex:
                    if j not in order:
                        for_cnt = False
                        break
                if for_cnt:
                    cnt += 1
            num_ex_str = "".join(num_ex)
            if cnt >= 2:
                cnt_dict[num_ex_str] = cnt
        cnt_dict = sorted(cnt_dict.items(), key=lambda x:x[1], reverse=True)
        if len(cnt_dict):
            start = cnt_dict[0][1]
        else:
            continue
        for i in cnt_dict:
            if start == i[1]:
                result.append(i[0])
            else:
                break
        
        for i in result:
            answer.append(i)

    answer.sort()
    return answer
