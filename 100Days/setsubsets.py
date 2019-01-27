def subsets(set_inp):
    if set_inp == []:
        return [[]]
    x = subsets(set_inp[1:])
    print(x)
    for y in x:
       z= 1+y
        print(z)
    return sorted( x + [[set_inp[0]] + y for y in x])
print(subsets([1,2,3]))
