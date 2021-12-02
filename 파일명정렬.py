def solution(files):

    answer = []
    information = []
    for i in files:
        temp = []
        for t in i:
            if t.isdigit():
                idx = i.index(t)
                break
        
        number = ""
        for z in i[idx:]:
            if z.isdigit():
                number += z
            else:
                break
        tmp_head = ""
        for j in i:
            if j in number:
                break
            else:
                tmp_head += j
        
        for_tail = tmp_head + number
        temp.append(tmp_head)
        temp.append(number)
        
        tail = i.replace(for_tail,"")
        temp.append(tail)
        information.append(temp)
    
    information.sort(key= lambda x:(x[0].lower(),int(x[1])))
    for i in information:
        text = ""
        for j in i:
            text += j
        answer.append(text)
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))

