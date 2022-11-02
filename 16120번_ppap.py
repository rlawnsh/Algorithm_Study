from collections import deque
start = deque(input())
p_cnt = 0
ap_cnt = 0

answer = ""
while start:
    check = start.popleft()
    if check == "P":
        p_cnt += 1
    else:
        if len(start) == 0:
            print("NP")
            exit(0)
        if start.popleft() != 'P':
            print("NP")
            exit(0)
        else:
            ap_cnt += 1
    if p_cnt <= ap_cnt:
        print("NP")
        exit(0)

if p_cnt - ap_cnt == 1:
    print("PPAP")
else:
    print("NP")

# 모범 답안

w = input()
stack = []
ppap = ["P", "P", "A", "P"]
for i in range(len(w)):
    stack.append(w[i])
    if stack[-4:] == ppap:
        for _ in range(4):
            stack.pop()
        stack.append("P")
if stack == ppap or stack == ["P"]:
    print("PPAP")
else:
    print("NP")

