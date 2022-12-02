def palindrome(temp):
    start, end = 0, len(temp) - 1
    while start <= end:
        if temp[start] == temp[end]:
            start += 1
            end -= 1
        else:
            return False
    return True
    
def solution(s):
    s = list(s)
    case = []
    for i in range(len(s)):
        start, end = i, len(s) - 1
        while start <= end:
            if s[start] == s[end]:
                temp = s[start:end+1]
                if palindrome(temp):
                    case.append(len(temp))
                    break
                else:
                    end -= 1
            else:
                end -= 1
                
    return max(case)