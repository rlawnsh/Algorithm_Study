def rotate(data):
    end = list(data[-1])
    mid = list(data[robot_out])
    left = end + data[:robot_out]
    right = mid + data[num:2*num]

    return left + right

num, k = map(int, input().split())
data = list(map(int, input().split()))
left_data = data[:num]
right_data = data[num:]
right_data = list(reversed(right_data))
data = left_data + right_data
robot_out = num-1
print(rotate(data))


