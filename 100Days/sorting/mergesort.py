def mergesort(arr):
    if len(arr)>1:
        n = len(arr)
        first = 0 
        last = n-1
        middle = (first+last)//2
        L = arr[first:middle+1]
        R = arr[middle+1:last+1]
        mergesort(L)
        mergesort(R)
    #i is the index for L j is for R and k is for the arr[]
        i = j = k =0
        while i < len(L) and j < len(R):
            if L[i]<R[j]:
                arr[k] = L[i]
                i+=1
                k+=1
            else:
                arr[k] = R[j]
                j+=1
                k+=1
        while i<len(L):
            arr[k] = L[i]
            k+=1
            i+=1
        while j<len(R):
            arr[k] = R[j]
            j+=1
            k+=1
    else:
        print("not greater than")
    return arr

arr = [2, 6, 1, 8, 5, 10]
print (mergesort(arr))