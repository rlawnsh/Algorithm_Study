'''

스택을 활용하여 짝지어 제거 가능

'''

def solution(s):
    new_s = []
    s = list(s)
    for i in s:
        if len(new_s) == 0:
            new_s.append(i)
        else:
            if new_s[-1] == i:
                new_s.pop()
            else:
                new_s.append(i)

    if len(new_s) == 0:
        return 1
    else:
        return 0