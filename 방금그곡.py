'''
import operator
for_answer = sorted(for_answer.items(), key=operator.itemgetter(1))

oprator를 import해서 딕셔너리 정렬을 value기준으로 해줄 수 있다. itemgetter(0)은 key값을 기준으로 정렬하게 된다.

'''

import operator
def m_replace(m):
    m = m.replace("C#", "c")
    m = m.replace("D#", "d")
    m = m.replace("F#", "f")
    m = m.replace("G#", "g")
    m = m.replace("A#", "a")
    return m

def solution(m, musicinfos):
    for_answer = {}
    answer = ""
    m = m_replace(m)

    arr = []
    for i in musicinfos:
        arr.append(i.split(","))
    for i in arr:
        for_true = True
        i[0] = i[0].split(":")
        i[1] = i[1].split(":")
        h = int(i[1][0]) - int(i[0][0])
        m1 = int(i[1][1]) - int(i[0][1])
        t = h*60 + m1
    
        i[3] = m_replace(i[3])
        n = len(i[3])
        if t >= n:
            cnt = t // n 
            cnt2 = t % n
        else:
            cnt = t
            for_true = False
        
        if for_true:
            i[3] = i[3] * cnt + i[3][:cnt2]
        else:
            i[3] = i[3][:cnt]
        
        if m in i[3]:
            for_answer[i[2]] = t
    
    for_answer = sorted(for_answer.items(), key=operator.itemgetter(1))
    
    if len(for_answer) > 1:
        if for_answer[0][1] == for_answer[-1][1]:
            answer = for_answer[0][0]
        else:
            for i in for_answer:
                if i[1] == for_answer[-1][1]:
                    answer = i[0]
                    return answer
    elif len(for_answer) == 1:
        answer = for_answer[0][0]
    else:
        return "(None)"
    
    return answer

