'''
Key Point = input num까지 0으로 채워진 임의의 배열(arr)을 만들어 배열의 index
가 num까지의 모든 숫자의 횟수를 담아내는데, arr[i] = arr[i-1] + 1이라고 하고(4번 째 규칙 -1을 한다) 
2, 3, 5 중 나눠질 경우와 비교하여 더 적은 값을 arr[i]에 저장을 한다.

'''

num = int(input())

arr = [0 for i in range(num+1)]

for i in range(2, num+1):
    arr[i] = arr[i-1] + 1

    if i % 2 == 0 and arr[i] > arr[i//2] + 1:
        arr[i] = arr[i//2] + 1
    if i % 3 == 0 and arr[i] > arr[i//3] + 1:
        arr[i] = arr[i//3] + 1
    if i % 5 == 0 and arr[i] > arr[i//5] + 1:
        arr[i] = arr[i//5] + 1
        
    
print(arr[num])
