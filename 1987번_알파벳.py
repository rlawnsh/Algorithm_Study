# import sys
# sys.setrecursionlimit(10**4)
# input = sys.stdin.readline
# answer = 0 

# a, b = map(int, input().split())
# data = []
# for i in range(a):
#     data.append(list(map(str, input().rstrip())))

# def dfs(x,y,cnt):
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
#     global answer
#     answer = max(answer, cnt)
    
#     for i in range(4):
#         if 0 <= x + dx[i] < a and 0 <= y + dy[i] < b and data[x+dx[i]][y+dy[i]] not in check:
#             check.add(data[x+dx[i]][y+dy[i]])
#             dfs(x + dx[i], y + dy[i], cnt + 1)
#             check.remove(data[x+dx[i]][y+dy[i]])

# cnt = 1
# check = set()

# check.add(data[0][0])
# dfs(0,0, cnt)
# print(answer)


import sys 
sys.setrecursionlimit(10000) 
def dfs(x, y, cnt): 
    dx = [1, -1, 0, 0] 
    dy = [0, 0, 1, -1] 
    now = (x, y) 
    
    global ans 
    ans = max(ans, cnt) 
    
    for i in range(4): 
        nx = now[0] + dx[i] 
        ny = now[1] + dy[i] 
        if(0 <= nx < R) and (0 <= ny < C): 
            if(done[strings[nx][ny]] == 0): 
                done[strings[nx][ny]] = 1 # print(done) 
                dfs(nx, ny, cnt+1) 
                done[strings[nx][ny]] = 0 #백트래킹 

R, C = map(int, input().split()) 
strings = [list(map(lambda x: ord(x)-65, input())) for _ in range(R)] # 아스키 코드로 바꿔줌 
done = [0]*26 # 알파벳 26개만큼 배열설정 
done[strings[0][0]] = 1 
ans = 1 
dfs(0, 0, ans) 
print(ans)
