def insertion(arr):
    for index in range(1, len(arr)):
        position = index
        current = arr[position]
        while position>0 and arr[position-1] > current:
            arr[position]=arr[position-1]
            position = position-1
        arr[position] = current
    return arr

arr = [5,4,7,1,8]
print (insertion(arr))