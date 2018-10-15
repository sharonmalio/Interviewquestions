def dupl(lst):
    newlst = list()
    for i in lst:
        if i not in lst:
            newlst.append(i)
        return len(newlst)

print (dupl((1, 1, 3, 5, 5, 7)))