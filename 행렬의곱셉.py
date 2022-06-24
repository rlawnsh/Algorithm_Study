def solution(arr1, arr2):
    answer = []
    new_arr2 = []
    for i in range(len(arr2[0])):
        temp = []
        for j in range(len(arr2)):
            temp.append(arr2[j][i])
        new_arr2.append(temp)
        
    for i in arr1: # i: [2,3,2]
        answer_temp = []
        for j in new_arr2: # j: [5,2,3]
            temp = 0
            for k in range(len(j)):
                temp += i[k] * j[k]
            answer_temp.append(temp)
        answer.append(answer_temp)
    return answer

################## 모범답안 #######################
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [ [ 1, 2 ], [ 2, 3 ]]
b = [[ 3, 4], [5, 6]]
print("결과 : {}".format(productMatrix(a,b)))