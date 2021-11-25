import sys
input = sys.stdin.readline

black = []
white = []

same = []
while True:
    try:
        b,w = map(int, input().split())
        if b == w:
            same.append(b)
        elif max(b,w) == b:
            if len(black) == 15:
                if min(black) < b:
                    black.remove(min(black))
                    black.append(b)
                else:
                    if len(white) == 15:
                        if min(white) < w:
                            white.remove(min(white))
                            white.append(w)
                    else:
                        white.append(w)
            else:
                black.append(b)
        else:
            if len(white) == 15:
                if min(white) < w:
                    white.remove(min(white))
                    white.append(w)
                else:
                    if len(black) == 15:
                        if min(black) < b:
                            black.remove(min(black))
                            black.append(b)
                    else:
                        black.append(b)
            else:
                white.append(w)
    except:
        break

for i in same:
    if min(black) <= min(white):
        if len(black) == 15 and min(black) < i:
            black.remove(min(black))
        black.append(i)
    elif min(black) > min(white):
        if len(white) == 15 and min(white) < i:
            white.remove(min(white))
        white.append(i)

print(sum(black) + sum(white))



import sys

info = []
for line in sys.stdin:info.append([int(e) for e in line.split()])
sz = len(info)
dp = [[[0 for _ in range(15+5)]for _ in range(15+5)]for _ in range(sz+1)]

for i in range(sz):
    for w in range(15+1):
        for b in range(15+1):
            if w+1 <= 15:
            	dp[i+1][w+1][b] = max(dp[i+1][w+1][b], dp[i][w][b]+info[i][0])
            if b+1 <= 15:
            	dp[i+1][w][b+1] = max(dp[i+1][w][b+1], dp[i][w][b]+info[i][1])
            dp[i+1][w][b] = max(dp[i+1][w][b], dp[i][w][b])

print(dp[sz][15][15])