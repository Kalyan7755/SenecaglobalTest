def eleorder(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            if arr.count(arr[i]) < arr.count(arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    return arr
arr = [1,4,5,6,6,5,3,5,1,6,4,6]
print(eleorder(arr))


