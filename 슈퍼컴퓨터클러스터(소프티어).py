# n, b = map(int, input().split())
# level = list(map(int, input().split()))

# start = min(level)
# end = b
# mid = b // 2

# while end - start > 1:
#     mid = (start + end) // 2
#     price = 0
#     escape = True
#     for i in level:
#         if i >= mid:
#             continue
#         else:
#             price += (mid - i) * (mid - i)
        
#         if price > b:
#             end = mid
#             escape = False
#             break

#     if escape:
#         start = mid 

# print(start)
n,b = map(int,input().split())
num_list= list(map(int,input().split()))
num_dict = {}

num_list = sorted(num_list,reverse=True)
left= num_list[-1]
right = 2000000000

for i in num_list:
    if(i not in num_dict.keys()):
        num_dict[i]=1
    else:
        num_dict[i]+=1



while(right-left>1):
    #left는 업그레이드 비용이 절대로 B를 넘지 않는다.
    #right는 업그레디으 비용이 절대로 B 아래가 되지 않는다.
    #때문에 right-left=1 이라는 것은 B를 넘지 않는 최대 효율이 left라는 것이다.
    mid = (right+left)//2
    cur_cost = 0
    isLeft = 1
    for k,v in num_dict.items():
        if(k<mid):
            cur_cost +=  ((mid-k)**2)*v
            if(cur_cost>b):
                right = mid
                isLeft=0
                break
    if(isLeft):
        left=mid

print(left)