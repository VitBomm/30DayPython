arr = []
for i in range(6):
    arr_1 = [int(index) for index in input().strip().split(' ')]
    arr.append(arr_1)

max_value = -9*8

for i in range(4):
    for j in range(4):
        kq = arr[i][j]+ arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if kq > max_value:
            max_value = kq

print(max_value)

