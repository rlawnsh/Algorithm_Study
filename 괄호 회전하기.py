def check(s):
    stack = []
    while len(s):
        end = s.pop()
        if end == '(' and len(stack) != 0:
            if stack.pop() != ')':
                return -1
        elif end == '{' and len(stack) != 0:
            if stack.pop() != '}':
                return -1
        elif end == '[' and len(stack) != 0:
            if stack.pop() != ']':
                return -1
        else:
            stack.append(end)
    if len(stack) != 0:
        return -1
    return 1

def solution(s):
    answer = 0
    s = list(s)
    for i in range(len(s)):
        if i == 0:
            s_copy = s.copy()
            ans = check(s_copy)
        else:
            s.append(s.pop(0))
            s_copy = s.copy()
            ans = check(s_copy)
            
        if ans == 1:
            answer += 1
    return answer