def selectionsort(arr):
    '''
        Starting from the first element, we search the smallest element in the array, and replace it with the element in the first position.
        We then move on to the second position, and look for smallest element present in the subarray, starting from index 1, till the last index.
        We replace the element at the second position in the original array, or we can say at the first position in the subarray, with the second smallest element.
        This is repeated, until the array is completely sorted.
    '''
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index]>arr[j]:
                min_index = j
            else:
                continue
        arr[i], arr[min_index] = arr[min_index],arr[i] 
                
    return arr
arr = [1, 9, 2, 5,10]
print (selectionsort(arr))