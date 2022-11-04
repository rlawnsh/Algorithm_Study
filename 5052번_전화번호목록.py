import sys

input = sys.stdin.readline

def solution():

    n = int(input())
    numbers = sorted([input().rstrip() for _ in range(n)])
    print(numbers)
    res = True
    for i in range(n-1):
        if(numbers[i+1].startswith(numbers[i])):
            res = False
            break
    
    print("YES" if res else "NO")

t = int(input())
for _ in range(t):         
    solution()