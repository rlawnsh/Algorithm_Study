'''
Key Point = 배열의 길이가 짝수라면 배열의 길이의 반을 m이라 했을 때,
배열을 반으로 나눠 왼쪽 부분과 오른쪽 부분의 각각의 인덱스의 차이는 m만큼 난다.

'''

num = list(map(int, input()))

left = 0
right = 0
mid = len(num)//2

for i in range(mid):
    left += num[i]
    right += num[mid + i]

if left == right:
    print("LUCKY")
else:
    print("READY")
