def for_notation(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        if mod == 10:
            rev_base += "A"
        elif mod == 11:
            rev_base += "B"
        elif mod == 12:
            rev_base += "C"
        elif mod == 13:
            rev_base += "D"
        elif mod == 14:
            rev_base += "E"
        elif mod == 15:
            rev_base += "F"
        else:
            rev_base += str(mod)

    return rev_base[::-1] 

def notation(num, end):
    start = 0
    find = ""
    while len(find) < end:
        temp = for_notation(start, num)
        if len(find + temp) > end:
            find += temp[:len(temp) - (len(find + temp) - end)]
        else:
            find += temp
        start += 1    
    return find        
    
def solution(n, t, m, p):
    answer = ''
    find = notation(n, t*m-1)
    find = "0" + find
    p -= 1
        
    for i in range(len(find)):
        if i == p:
            answer += find[i]
            p += m
        
    return answer