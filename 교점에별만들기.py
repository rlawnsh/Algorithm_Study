'''

이차원 리스트를 리스트 컴프리핸션으로 만들 때 => answer = [["."] * star for i in range(star_height)]
람다식 => inter_0 = list(map(lambda x: x[0], inter))

'''

from itertools import combinations

def solution(line):
    inter = []
    answer = []
    case = list(combinations(line,2))
    for i in case:
        A = i[0]
        B = i[1]
        a, b, e = A[0], A[1], A[2]
        c, d, f = B[0], B[1], B[2]
        inter = intersection(a, b, e, c, d, f, inter)
    inter = list(set(inter))
    inter_0 = list(map(lambda x: x[0], inter)) # inter[0]로만 이루어진 리스트 만들기, x값들의 모임
    inter_1 = list(map(lambda x: x[1], inter)) # inter[1]로만 이루어진 리스트 만들기, y값들의 모임
    
    star = max(inter_0) - min(inter_0) + 1          # .의 개수를 세기 위해 x좌표 최댓값과 최솟값 찾기
    star_height = max(inter_1) - min(inter_1) + 1   # 격좌의 높이를 정하기위해 y좌표 최댓값과 최솟값 찾기
    
    answer = [["."] * star for i in range(star_height)]
    
    answer_x_0 = -min(inter_0) # . 중에서 인덱스 0을 정해주기 위해
    answer_y_start = max(inter_1) # 격좌의 높이에서 인덱스 처리하기 위해
    
    for i in inter:
        x = i[0]
        y = i[1]
        answer[answer_y_start - y][answer_x_0 + x] = "*"
    
    answer = list(map(lambda x: ''.join(x), answer))
    return answer

def intersection(a, b, e, c, d, f, inter):
    if a*d-b*c != 0:
        x = (b*f-e*d)/(a*d-b*c)
        y = (e*c-a*f)/(a*d-b*c)
    else:
        return inter
    if int(x) == x and int(y) == y:
        inter.append((int(x),int(y)))
    return inter

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))

