import sys
input = sys.stdin.readline

n = int(input())
people = []
buyId = 1
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if j % 2 == 1:
            people.append([temp[j], temp[j+1], buyId])            
    buyId += 1
people.sort()

m = int(input())
temp = list(map(int, input().split()))
m_list = []
Sid = 1
for i in temp:
    m_list.append([i, Sid])
    Sid += 1
m_list.sort()

# print(m_list)
# print(people)

revenue = 0
people_pay = [0] * (n+1)
mId = 0
for i in range(len(people)):
    size, pay, Pid = people[i][0], people[i][1], people[i][2]
    if people_pay[Pid] < pay:
        revenue += pay - people_pay[Pid]
        people_pay[Pid] = pay
    while mId < m and m_list[mId][0] <= revenue:
        m_list[mId].append(size)
        mId += 1

m_list.sort(key = lambda x:x[1])
for i in m_list:
    if len(i) >= 3:
        print(i[-1], end= " ")
    else:
        print(-1, end= " ")

