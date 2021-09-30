'''

2차원 list sizes를 1차원 list new_sizes로 바꾸는 방법 : new_sizes = sum(sizes, [])

'''

def solution(sizes):
    new_sizes = sum(sizes, [])
    a = max(new_sizes)
    
    arr = []
    
    for i in sizes:
        arr.append(min(i))
    
    b = max(arr)
    answer = a*b
    return answer