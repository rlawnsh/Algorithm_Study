import heapq
def solution(operations):
    answer = []
    heap = []
    
    for i in operations:
        op = i.split(" ")
        if op[0] == "I":
            heapq.heappush(heap, int(op[1]))
        else:
            if op[1] == "-1" and len(heap):
                heapq.heappop(heap)
            elif op[1] == "1" and len(heap): 
                temp = []
                while heap:
                    temp.append(heapq.heappop(heap))
                temp.pop()
                heapq.heapify(temp)
                heap = temp
    if len(heap):
        answer = [max(heap), min(heap)]
    else:
        answer = [0,0]
    return answer