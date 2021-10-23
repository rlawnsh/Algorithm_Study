arr = []
for i in range(3):
    if i == 0:
        arr.append(int(input()))
    if i == 1:
        arr.append(list(map(int, input().split())))
    if i == 2:
        arr.append(input())

grade = {"B": arr[1][0]-1, "S": arr[1][1]-1, "G": arr[1][2]-1, "P": arr[1][3]-1, "D": arr[1][3]}
answer = grade[arr[2][0]]

for i in range(1, len(arr[2])):
    if arr[2][i] == "D":
        answer += arr[1][3]
        continue
    if i == 1:
        tmp = grade[arr[2][i]] - answer
    else:
        tmp = grade[arr[2][i]] - tmp
    answer += tmp

print(answer)