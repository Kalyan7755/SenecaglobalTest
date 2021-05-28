def order(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1
    return arr
arr = [1, 2, -4, 0, -1, 0, 3, 7, 0, 5, 0, 1, -1, 0]
print(order(arr))


