import sys
input = lambda : sys.stdin.readline().strip()

n, p=map(int,input().split())
a=[list(map(int,input().split())) for i in range(n)]

c=0
ch=[[] for i in range(7)]

for i,j in a:
    if len(ch[i]) == 0:
        ch[i].append(j)
        c +=1
        
    else:
        if j > ch[i][-1]:
            ch[i].append(j)
            c += 1
        elif j == ch[i][-1]: # 이미 있는 경우
            continue
        else: 
            while len(ch[i]) != 0 and j < ch[i][-1]:
                ch[i].pop()
                c += 1
            if len(ch[i]) != 0 and ch[i][-1] == j:
                continue
            ch[i].append(j)
            c += 1

print(c)