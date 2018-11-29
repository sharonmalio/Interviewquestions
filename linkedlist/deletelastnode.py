class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.prev=None
        self.len = 0

    # def addnodes(self, data):
    #     temp = self.head
    #     if temp is None:
    #        temp = Node(data)
    #     else:
    #         temp.next=Node(data)
    #         temp = temp.next
    #     return temp

    def addnodes(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return new_node

    def findlength(self):
        self.len = 0
        temp= self.head
        while temp:
            temp=temp.next
            self.len +=1
        return self.len 

    # def deletemiddle(self, key):
    #     curr = self.head
    #     prev = None

    #     while prev is not None:
    #         if curr.data == key:
    #             prev.next = curr.next
    #         else:
    #             prev = curr
    #             curr = curr.next
    #     return False 

    # def getnthNode(self, index):
    #     nodeindex = 0
    #     temp = self.head
    #     while temp:
    #         if nodeindex == index:
    #             return temp.data
    #         else:
    #             nodeindex+=1
    #             temp = temp.next
    #     return temp.data

    # def deletefirst(self):
    #     temp=self.head
    #     while temp:
    #         temp.next = self.head
    #         return temp.next

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
    # def deletenthFromlast(self, value):
    #     position =1 
    #     temp = self.head
    #     while value < self.len:
    #         if (len - value + 1)==position:
    #             temp.next =  self.head
    #         else:
    #             temp = temp.next
    #             position += 1
    #     return temp
    def nthFromLast(self, n):
        curr = self.head
        i=0
        while i<(self.len-n):
            curr=curr.next
            i+=1
        return curr
            


        
# Driver program 
llist = Linkedlist() 
llist.addnodes(7) 
llist.addnodes(1) 
llist.addnodes(3) 
llist.addnodes(2) 
  
print ("origial list: ")
llist.printlist() 
 

llist.addnodes(4)
print("nth to last:")
llist.nthFromLast(2)
print ("After adding 4: ")
llist.printlist() 
  