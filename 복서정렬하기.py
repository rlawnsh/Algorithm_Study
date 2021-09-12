'''

2차원 배열을 정렬할 때 람다를 활용해서 경우의 수를 모두 따져서 정렬 할 수 있고, -는 내림차순이다.
info.sort(key=lambda x: (-x[0],-x[1],-x[2],x[3]))

'''

def solution(weights, head2head):
    info = []
    for i in range(len(weights)):
        win = 0
        win_heavy = 0
        divide = len(weights) - 1
        player = []
        for j in range(len(head2head)):
            if i == j:
                continue
            if head2head[i][j] == "W":
                win += 1
                if weights[i] < weights[j]:
                    win_heavy += 1
            elif head2head[i][j] == "N":
                divide -= 1
        if divide == 0:
            win_per = 0
        else:
            win_per = win/divide
        player.extend([win_per, win_heavy, weights[i], i+1])
        info.append(player)
    
    info.sort(key=lambda x: (-x[0],-x[1],-x[2],x[3]))
    answer = []
    for i in info:
        answer.append(i[3])
    return answer

print(solution([50,82,75,120], 	["NLWL","WNLL","LWNW","WWLN"]))