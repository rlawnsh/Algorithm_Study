# 풀이 1

def solution(s):
    s = s.split("}")
    for i in range(len(s)):
        s[i] = s[i].replace("{", "")
        s[i] = s[i].split(",")
        for j in s[i]:
            if j == "":
                s[i].remove("")

    s.sort(key=lambda x:len(x))
    answer = []
    for i in s:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))

    return answer

# 더 좋은 풀이 2
'''

Python - String strip(), rstrip(), lstrip() 사용

'''

def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split("},{")

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer

# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))