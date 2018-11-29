import unittest
def multiplication(num):
   
    for i in range(num + 1,1,-1):
        for j in range(1, num+1):
            print(i*j, end="\t")
        print("\n")

print(multiplication(3))