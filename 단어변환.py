from collections import deque
def find_check(begin, words, len_word, check):
    for i in words:
        ans = 0
        for j in range(len_word):
            if len(i) == 0:
                continue
            if begin[j] == i[j]:
                ans += 1
        if ans == len_word - 1:
            check.append(i)
            words[words.index(i)] = ""
    return check

def solution(begin, target, words):
    answer = 0
    len_word = len(begin)
    check = deque([])
    
    check = find_check(begin, words, len_word, check)
    if len(check) > 0:
        answer += 1
    else:
        return 0
    
    while check:
        c_p = check.popleft()
        if c_p == target:
            return answer
        for_answer = len(check)
        check = find_check(c_p, words, len_word, check)
        if len(check) > for_answer:
            answer += 1
    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))