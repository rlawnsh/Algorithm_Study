import sys
input = sys.stdin.readline

n, k = map(int, input().split())
chocolate = list(map(int, input().split()))
chocolate.append(0)
chocolate.sort()

eat = 0
day = 0
start = 1
while True:
    escape = False
    tmp_eat = eat
    for i in range(start,len(chocolate)):
        if i-k > 0 and chocolate[i] != chocolate[i-k]:
            tmp_chocolate = chocolate[i-k]
            eat += chocolate[i] - tmp_chocolate
            chocolate[i] = tmp_chocolate
            if tmp_eat != eat:
                day += 1
            chocolate.sort()
            start = i
            break
        elif len(set(chocolate)) == 2:
            escape = True
            break
    if escape:
        break

print(eat, day)

        

