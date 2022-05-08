def correct(s):
    c_t = 0
    while s:
        if s.pop(0) == "(":
            c_t += 1
        else:
            c_t -= 1
        if c_t < 0:
            return False
    return True

def solution(p):
    answer = ''
    
    if len(p) == 0:
        return ""
    list_p = list(p)
    m = list_p.copy()
    if correct(m):
        return "".join(list_p)
    
    u = []
    v = []
    a = 0
    for i in list_p:
        if i == "(":
            a += 1
        else:
            a -= 1
        u.append(i)           
        if a == 0:
            break
    v = list_p[len(u):]
    copy_u = u.copy()
    if correct(copy_u) == True:
        answer= "".join(u) + "".join(solution("".join(v)))
    else:
        empty = "("
        empty += solution("".join(v))
        empty += ")"
        u.pop(0)
        u.pop(-1)
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        empty += "".join(u)
        answer = empty
    
    return answer

print(solution("()))((()"))

