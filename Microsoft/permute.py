print('Hello world - Python!')

def getInput():
    f = open('words.txt', 'r')
    for line in f:
        print (line)
        words = line.replace('"', '').split(",")
        print(words)
        # for word in words:
        #     print(word)

        original = words[0]
        permutated = words[1]

# def Permutation():
getInput()

