import copy

def solution(n, wires):
    sub_list = [] # 모든 경우에 따른 전력망의 차
    stop = 0
    
    while stop < len(wires): 
        sub = 0
        new_wires = copy.deepcopy(wires)        
        slice_wires = []                        # 한 경우에서 잘려진 전력망 리스트
        slice_wires.append(new_wires[stop][0])
        new_wires.pop(stop)
        while slice_wires:
            sub += 1
            s_p = slice_wires.pop(0)
            for_pop = []                        # new_wires에서 빼주기 위해
            for i in range(len(new_wires)):
                if s_p in new_wires[i]:
                    for_pop.append(i)
                    if s_p == new_wires[i][0]:
                        slice_wires.append(new_wires[i][1])
                    else:
                        slice_wires.append(new_wires[i][0])
                    
            for i in for_pop:
                new_wires.pop(i)
                for j in range(len(for_pop)):
                    for_pop[j] -= 1
        sub_list.append(abs(n-(2*sub)))
        stop += 1
        
    answer = min(sub_list)
    return answer

print(solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
