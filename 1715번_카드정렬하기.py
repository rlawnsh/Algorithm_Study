import heapq
n = int(input())
card = []
for i in range(n):
    heapq.heappush(card, int(input()))

ans = []
while len(card) > 1:
    a, b = heapq.heappop(card), heapq.heappop(card)
    c = a+b
    ans.append(c)
    heapq.heappush(card, c)

print(sum(ans))