from collections import deque

def solution(enroll, referral, seller, amount):
    enroll_earn = dict()
    tree = dict()

    for e in enroll:
        enroll_earn[e] = 0
    
    for r in range(len(referral)):
        if referral[r] == "-":
            tree[enroll[r]] = 'center'
        else:
            tree[enroll[r]] = referral[r]
    
    for s in range(len(seller)):
        que = deque()
        money = amount[s] * 100
        que.append(seller[s])
        while que:
            q = que.popleft()
            if money * 0.1 < 1:
                enroll_earn[q] += money
                break
            else:
                minus = int(money*0.1)
                enroll_earn[q] += money - minus
                if tree[q] == 'center':
                    break
                else:
                    que.append(tree[q])
                money = minus
    answer = list(enroll_earn.values())
    return answer