def bubblesort(inp):
    '''
    compare the first two elements, if the element at position+1 is less swap the positions wth the one at position
    '''
    n=len(inp)
    swapped = False
    for i in range(n):
        for j in range(0,n-i-1):
            if inp[j]>inp[j+1]:
                inp[j],inp[j+1] = inp[j+1],inp[j]
                swapped = True
    return inp
inp =  [64, 34, 25, 12, 22, 11, 90]
print(bubblesort(inp))