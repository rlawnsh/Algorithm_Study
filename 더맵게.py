import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    for j in range(len(scoville)):
        if len(scoville) == 1:
            if scoville[0] < K:
                answer = -1
            break
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        if first >= K:
            break
        heapq.heappush(scoville, first + second*2)
        answer += 1
        
    return answer

print(solution([10,1,3,2,12,9], 7))