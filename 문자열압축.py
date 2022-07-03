def find_case(temp): # ["ab", "ab", "cd", "cd"]
    same = 0
    temp_case = ""
    start = temp[0]
    for i in temp:
        if start == i:
            same += 1
        else:
            if same == 1:
                temp_case += start
                start = i
                same = 1
            else:
                temp_case += str(same) + start
                start = i
                same = 1
    if same == 1:
        temp_case += start
    else:
        temp_case += str(same) + start
    return temp_case

def solution(s):
    answer = 0
    len_s = len(s)
    start = 1
    case = []
    while start <= len_s:
        copy_s = s
        copy_s = list(copy_s)
        temp = []
        step = ""
        for i in copy_s:
            step += i
            if len(step) == start:
                temp.append(step)
                step = ""
        if len(step) > 0:
            temp.append(step)
        
        case.append(find_case(temp))
        start += 1
    
    case.sort(key=lambda x:len(x))
    answer = len(case[0])
    return answer