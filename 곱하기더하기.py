'''

Key Point : 0은 덧셈에도 영향을 주지 않기 때문에 0을 아예 없애주고 시작

'''
num = input()
num = num.replace('0','') 
num = list(map(int, num))

a = num.pop(0)
b = num.pop(0)

answer = 0
if a == 1 or b == 1:
    answer = a + b
else:
    answer = a * b

for i in num:
    if i == 1:
        answer += i
    else:
        answer *= i


print(answer)
