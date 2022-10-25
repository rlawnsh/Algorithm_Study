# 풀이 1 - combinations

# from itertools import combinations

# l, c = map(int, input().split())
# alpha = list(map(str, input().split()))
# alpha.sort()

# check = ['a', 'e', 'i', 'o', 'u']

# case = list(combinations(alpha, l))
# answer = []
# for i in case:
#     cnt = 0
#     for j in i:
#         if j in check:
#             cnt += 1
#     if cnt >= 1 and len(i) - cnt >= 2:
#         answer.append(''.join(i))

# for i in answer:
#     print(i)

# 풀이 2 - backtracking

def backtracking(password, level, idx):
    if level == l:
        cnt = 0
        for i in password:
            if i in check:
                cnt += 1
        if cnt >= 1 and len(password) - cnt >= 2:
            print(''.join(password))

        return
    
    else:
        for i in range(idx, len(alpha)):
            if visit[i] == False:
                password.append(alpha[i])
                visit[i] = True
                backtracking(password, level + 1, i+1)
                password.pop()
                visit[i] = False

l, c = map(int, input().split())
alpha = list(map(str, input().split()))
alpha.sort()
check = ['a', 'e', 'i', 'o', 'u']
level = 0
visit = [False] * c
password = []
backtracking(password, level, 0)