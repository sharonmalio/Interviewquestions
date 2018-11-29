import unittest
def square(num):
    n_list = [[num for i in range(num+1)]for j in range(num+1)]
    for x in range(num+1):
        for y in range(num+1):
            print(n_list[i][j])

        print()
    
if __name__ == '__main__':
    print (square(3))
