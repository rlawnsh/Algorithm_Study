from collections import deque
def solution(fees, records):
    st = fees[0]
    sf = fees[1]
    at = fees[2]
    af = fees[3]
    
    records = [i.split(" ") for i in records]
    records.sort(key=lambda x:x[1])
    
    records = deque(records)
    answer = []
    time = 0
    car_num = records[0][1]

    for_while = True
    if len(records) == 1:
        records = records[0][0].split(":")
        answer.append((23 - int(records[0]))*60 + (59 - int(records[1])))
        for_while = False
    while records and for_while:
        car_in = records.popleft()
        in_time = car_in[0].split(":")
        if len(records) == 0:
            if car_in[1] == car_out[1]:
                answer[-1] += (23 - int(in_time[0]))*60 + (59 - int(in_time[1]))
            else:
                answer.append((23 - int(in_time[0]))*60 + (59 - int(in_time[1])))
            break

        car_out = records.popleft()
        out_time = car_out[0].split(":")
        
        if car_num != car_in[1]:
            car_num = car_in[1]
            answer.append(time)
            time = 0
        
        if car_out[2] == "IN":
            time += (23 - int(in_time[0]))*60 + (59 - int(in_time[1]))
            answer.append(time)
            car_num = car_out[1]
            if len(records) == 0:
                answer.append((23 - int(out_time[0]))*60 + (59 - int(out_time[1])))
                break
            records.appendleft(car_out)
            time = 0
            
        else:
            time += (int(out_time[0]) - int(in_time[0]))*60 + (int(out_time[1]) - int(in_time[1]))
            if len(records) <= 1:
                answer.append(time)
    
    result = []
    for t in answer:
        if (t - st) % at:
            up = 1
        else:
            up = 0
        if t <= st:
            result.append(sf)
        else:
            result.append(sf + ((t-st)//at + up) * af)

            
    return result



print(solution([120,0,60,591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))