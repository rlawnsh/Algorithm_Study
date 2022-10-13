from copy import deepcopy


def permutation(N, M, level):
    if level == M:
        print(result)
        t = deepcopy(result)
        
        temp.append(t)
        return

    for i in range(N):
        if check[i] == False:
            check[i] = True  # 이 줄이랑~
            result[level] = list[i]
            permutation(N, M, level + 1)
            check[i] = False # ~ 이 줄 없으면 중복 허용

N = 4
M = 3                    # N개중 M개 뽑기
list = [10, 20, 30, 40]  # 입력 배열
result = [0] * M         # 출력 배열
check = [False] * N      # 방문 확인 배열
temp = []
# print(permutation(N, M, 0))
# print(temp)

def combination(N, M, level, idx):
    if level == M:
        print(result)
        return

    for i in range(idx, N):
        result[level] = list[i]
        combination(N, M, level + 1, i + 1)

print(combination(N, M, 0, 0))