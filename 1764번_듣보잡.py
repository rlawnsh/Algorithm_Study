import sys
input = sys.stdin.readline

d, b = map(int, input().split())

d_arr = set()
b_arr = set()

for i in range(d):
    d_arr.add(input().rstrip())

for i in range(b):
    b_arr.add(input().rstrip())

answer = list(d_arr & b_arr)
answer.sort()
print(len(answer))
for i in answer:
    print(i)


