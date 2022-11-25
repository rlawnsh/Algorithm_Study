import heapq
def solution(n, works):
    answer = 0
    heap = []
    for i in works:
        heapq.heappush(heap, -i)
        
    for i in range(n):
        heap_pop = -heapq.heappop(heap)
        if heap_pop == 0:
            break
        heapq.heappush(heap, -(heap_pop - 1))
        
    for i in heap:
        answer += i * i
    return answer