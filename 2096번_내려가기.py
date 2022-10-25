n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    if i == 0:
        for_min = [a,b,c]
        for_max = [a,b,c]
    else:
        min_a, min_b, min_c = for_min[0], for_min[1], for_min[2]
        max_a, max_b, max_c = for_max[0], for_max[1], for_max[2]
        for j in range(3):
            if j == 0:
                for_min[j] = min(min_a+a, min_b+a)
                for_max[j] = max(max_a+a, max_b+a)
            elif j == 1:
                for_min[j] = min(min_b + b, min_a + b, min_c + b)
                for_max[j] = max(max_b + b, max_a + b, max_c + b)
            elif j == 2:
                for_min[j] = min(min_c + c, min_b + c)
                for_max[j] = max(max_c + c, max_b + c)

print(str(max(for_max)) + " " + str(min(for_min)))