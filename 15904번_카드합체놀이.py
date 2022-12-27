import heapq

n, m = map(int, input().split())

number = list(map(int, input().split()))
heapq.heapify(number)
for i in range(m):
    a, b = heapq.heappop(number), heapq.heappop(number)
    heapq.heappush(number, a+b)
    heapq.heappush(number, a+b)

print(sum(number))