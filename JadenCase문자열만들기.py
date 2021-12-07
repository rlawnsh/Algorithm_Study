'''

a = "i am junoh kim"
print(a.title())
->I Am Junoh Kim
title 내장함수를 이용해 각 영단어의 첫 글자를 대문자로 바꿀 수 있음

'''

def solution(s):
    lower_s = s.lower()
    arr = []
    for i in lower_s:
        arr.append(i)

    uppercase = True
    answer = ''
    for i in range(len(arr)):
        if uppercase == False and arr[i] != " ":
            answer += arr[i]
            continue
        if arr[i] == " ":
            uppercase = True
        else:
            arr[i] = arr[i].upper()
            uppercase = False
        answer += arr[i]
    
    return answer

