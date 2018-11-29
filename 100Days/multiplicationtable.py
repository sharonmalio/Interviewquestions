import unittest
def multiplication(num):
    string = ""
    for i in range(1, num+1):
        for j in range(num, 0, -1):
            string +=  "{}\t".format(i*j, end="\t")
        string += "\n"
    print(string)
print(multiplication(3))
