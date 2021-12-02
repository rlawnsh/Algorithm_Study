import sys
input=sys.stdin.readline

n=int(input())
mn=[]
mx=[]
data=[]
for _ in range(n):
    a,b=map(int,input().split())
    data.append([a,b])
    mn.append(a-b)
    mx.append(a+b)
mn.sort()
mx.sort()

def binary_search(k):
    start=0
    end=n-1
    result=-1
    while end>=start:
        mid=(start+end)//2
        if mx[mid]>=k:
            end=mid-1
        else:
            result=max(result,mid)
            start=mid+1
    return result+2

def binary_search2(k):
    start=0
    end=n-1
    result=-1
    while end>=start:
        mid=(start+end)//2
        if mn[mid]<=k:
            result=max(result,mid)
            start=mid+1
            
        else:
            end=mid-1
    return result+1
for i in data:
    print(binary_search(i[0]-i[1]),binary_search2(i[0]+i[1]))