'''

다른 사람의 풀이중에 괜찮은 풀이가 있어 차용해 봤다. solution2에서 파이썬 list comprehension을 이용하여 한줄로 코드가 간결해 졌다. 
그리고 sum을 활용하여 배열의 값을 한번에 계산한다.

'''

def solution(price, money, count):
    for_price = 0
    for i in range(1,count+1):
        for_price += price * i
        
    if money - for_price > 0:
        return 0
    else:
        return -(money - for_price)

def solution2(price, money, count):
    return abs(min(money - sum([price*i for i in range(1,count+1)]),0))



