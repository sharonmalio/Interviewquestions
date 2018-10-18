def subsets(set_inp):
    if set_inp == []:
        return [[]]
    x = subsets(set_inp[1:])

    return sorted( x + [[set_inp[0]] + y for y in x])
print(subsets([1,2,3]))
