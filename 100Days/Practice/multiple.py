"""Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise."""
# def is_multiple(n, m):
#     if m%n == 0:
#         return True
#     else:
#         return False
# print(is_multiple(2, 5))
num = 24
num = num/2
def positivesquares(n):
    sum = 0
    for i in range(1, n):
        sum = sum+(i*i)
    return sum
print(positivesquares(4))

def double(n):
    for i in range(1, n):
        if i%2==0:
            print(i*2)
        else:
            pass
print(double(8))
#reverse a number
def reverse(num):
    reversed = 0
    while num>0:
        reversed = (reversed*10) + num%10
        num =  num//10
    return reversed
print(reverse(1234))

#  reverses a list of integers

def reverse2(list1):
    reversed = []
    length =  len(list1)
    for i in list1:
        reversed. append(list1[length-1])
        length -= 1
    return reversed
print(reverse2([1,2,3,4]))

def oddproduct(list1):
    index = 0
    while index >= 0:
        if (list1[index]*list1[index+1]%2 != 0):
            tuplle = (list1[index], list1[index+1])
            index += 1
        return tuplle
print(oddproduct([1, 3, 4, 5]))
        
def alphabets():
    for x in range(ord("a"), ord("z")):
        print(chr(x))


        