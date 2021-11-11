from itertools import combinations
from copy import deepcopy
num = int(input())
data = []
person = [i for i in range(num)]
person_case = list(combinations(person, num//2))
print(person_case)
for i in range(num):
    data.append(list(map(int, input().split())))

answer = []
for i in range((len(person_case)//2)+1):
    a, b, c, d = 0, 0, 0, 0
    tmp_person = deepcopy(person)
    tmp_person_case = deepcopy(person_case[i]) # [0,2,5]
    team1_combination = list(combinations(person_case[i], 2)) #[(0,2), (0,5), (2,5)]
    team1 = 0
    team2 = 0
    for j in team1_combination:
        a, b = j[0], j[1]
        team1 += data[a][b] + data[b][a]
    for k in tmp_person_case:
        tmp_person.remove(k) # [1,3,4]
    
    team2_combination = list(combinations(tmp_person, 2))
    for t in team2_combination:
        c, d = t[0], t[1]
        team2 += data[c][d] + data[d][c]
    answer.append(abs(team1 - team2))

print(min(answer))

    
    



