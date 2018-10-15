def reverse(inputString):
    return inputString[::-1]
inputString = [2, 5, 7, 9]
print (reverse(inputString))

# inputString = input("Enter input string: ")
# if(len(inputString) == 0):
#     print("Inavlid string")
# elif (len(inputString) == 1):
#     print(inputString)
# else:
#    print (reverse(inputString))

def multiplication(num):
    for i in range(1, num+1):
        for j in range(1, num+1):
            print(i*j, end = '\t')
        print()
# print(multiplication(12))

def addFile():
    file = open('integers.txt', 'r')
    s = 0
    
    for line in file.read().splitlines():
        line = line.strip()
        print (line)
        i = int(line)
        s += i
    print (s)
    file.close()

# addFile()

# def sum_file(filename):
#   return (sum(int(l) for l in open(filename).readlines()))

# sum_file('integers.txt')

def largest(intArr):
    maxInt = intArr[0]
    for i in intArr:
        if (i > maxInt):
           maxInt = i
    print (maxInt)
 
    
intAr = [34, 78, 134, 27, 90]
# print (largest(intAr))


def reverse2(num):
  rev = 0
  while num > 0:
    rev = (10*rev) + num%10
    num /= 10
  return rev

print(reverse2(21))

def isPalindrome(num, rev):
    return num == rev  

def palindrome(num):
    while(num < 1000000):
        rev = reverse(num)
        if (isPalindrome(num, rev) is True):
            print("is palindrome")
            return True
        else:
            num = num + rev
            num = 0
            num += 1
            print("is palindrome after %d", (num))
    return False 
#print(palindrome(19))


def cipher(inputStr):
    words = inputStr.split(":")

    offset = int(words[0])
    print("Offset is: ", offset)

    message = words[1]
    print("Message is: ", message)

    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += offset

            if symbol.isupper():
                if num > ord('Z'):
                    num -=26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -=26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        elif symbol.isdigit:
            num = ord(symbol)
            num += offset
            if num > ord('9'):
                num -= 9
            elif num < ord('0'):
                num += 9
            translated += chr(num)
        else:
            translated += symbol

    return translated

#print(cipher("3:WBdv4"))

def stringcut(string1):
    plaintext =string1.split(":")
    offset= int(plaintext[0])
    word = plaintext[1]
    print( "offset is:", offset)
    print("word is:", word)

    return plaintext
    # OriString = "1:WSPf"
    # print(stringcut(OriString))

# def caesar(word, offset):
#     cipherText=""
#     for ch in word:
#         if ch.isalpha():
#             stayInAlphabet = ord(ch) + offset
#             if stayInAlphabet > ord('z'):
#                 stayInAlphabet -= 26
#             finalLetter = chr(stayInAlphabet)
#             cipherText += finalLetter
#     print("Your ciphertext is: ", cipherText)
#     return cipherText
# plaintext= stringcut("3:WRVVVBdgfv")
# word = plaintext[1]
# offset= int(plaintext[0])
#caesar(word, offset)
NO_OF_CHARS = 256
def substring(string):
    n = len(string)
    curr_len = 0
    max_leng = 0
    prev_index = 0
    i = 0

    visited =[-1] * NO_OF_CHARS

    visited[ord(string[0])] = 0
    for i in range(1, n):
        prev_index = visited[ord(string[i])]

        if prev_index == -1 or (i - curr_len > prev_index):
            curr_len += 1
        else:
            if curr_len > max_leng:
                max_leng = curr_len
            curr_len = i - prev_index
        visited[ord(string[i])] = i

    if curr_len > max_leng:
        max_leng = curr_len

    return max_leng
#print(substring("abbhuibghh"))

# def rob(arr):
#     maxInt =  max(arr)
#     for i in arr:

# arr = [8, 9, 3]
# rob(arr)


