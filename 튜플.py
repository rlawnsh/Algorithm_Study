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