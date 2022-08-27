def solution(dirs):
#     (5,5) / (5,6) / (4,6) / (4,7) / (5,7) / (6,7) / (6,6) / (5,6) / (4,6) / (4,7)
#     (5,5,5,6)
    idx = [[0,1], [0,-1], [1,0], [-1,0]]
    start = [5,5]
    way = [[5,5]]
    for i in dirs:
        start = start.copy()
        if i == "U":
            if 0 <= start[0] + idx[0][0] <= 10 and 0 <= start[1] + idx[0][1] <=10:
                start[0] += idx[0][0]
                start[1] += idx[0][1]
                way.append(start)
        elif i == "D":
            if 0 <= start[0] + idx[1][0] <= 10 and 0 <= start[1] + idx[1][1] <= 10:
                start[0] += idx[1][0]
                start[1] += idx[1][1]
                way.append(start)
        elif i == "R":
            if 0 <= start[0] + idx[2][0] <= 10 and 0 <= start[1] + idx[2][1] <= 10:
                start[0] += idx[2][0]
                start[1] += idx[2][1]
                way.append(start)
        elif i == "L":
            if 0 <= start[0] + idx[3][0] <= 10 and 0 <= start[1] + idx[3][1] <= 10:
                start[0] += idx[3][0]
                start[1] += idx[3][1]
                way.append(start)
    
    new_way = []
    for i in range(len(way)-1):
        temp = way[i] + way[i+1]
        temp2 = way[i+1] + way[i]
        if temp not in new_way and temp2 not in new_way:
            new_way.append(temp)
        
    answer = len(new_way)
    return answer
