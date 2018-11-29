def maxi(inp) :  
    # Initializing max alphabet to 'a' 
    max = 'A'
    size = len(inp)
    # Find largest alphabet 
    for i in range(size) :  
        if (inp[i] > max): 
            max = inp[i] 
  
    # Returning largest element 
    return max
print(maxi("axe"))