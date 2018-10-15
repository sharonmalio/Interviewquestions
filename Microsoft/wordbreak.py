def wordbreak(inputstr, dictwords):
    length = len(inputstr)
    substr = list()
    for i in range(length):
        for j in range(i, length):
            substr.append(inputstr[i:j + 1])
    # print (substr)
    
    for s in substr: 
        if s in dictwords:
            print(s)

inputstr = 'carsgofast'
dictwords = {'cars', 'go', 'fast'}
wordbreak(inputstr,dictwords )