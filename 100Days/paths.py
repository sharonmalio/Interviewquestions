def numOfPaths(n,m):
    count = 0
    if m==1 and n == 1:
        return 1
    else:
        while n >= 1 and m >= 1:
            if m-1 and n or  n-1 and m:
                count += 1
        
        return count
print numOfPaths(3,3)