class Node:

    def __init__(self,data):

        self.data = data
        self.next = None

class CLL:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self,data):
        node = Node(data)
        self.size +=1
        if self.head == None:
            node.next = node
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.tail.next = node
        self.head = node

    def add_last(self,data):
        node = Node(data)
        self.size +=1
        if self.tail == None:
            self.add_first(data)
            return
        self.tail.next = node
        node.next = self.head
        self.tail = node

    def insert(self,index,data):
        node = Node(data)
        self.size +=1
        if index == 0:
            self.add_first(data)
        elif index==self.size-1:
            self.add_last(data)
        else:
            head = self.head
            for itr in range(index-1):
                head = head.next
            node.next = head.next
            head.next = node

    def removefirst(self):
        temp = self.head
        self.head = temp.next
        self.tail.next = self.head

    def removelast(self):
        head = self.head
        self.size -=1
        for itr in range(self.size-1):
            head = head.next
        head.next = self.head
        self.tail = head

    def removeAt(self,index):
        head = self.head
        pre = self.head
        if index == 0:
            self.removefirst()
            return
        
        if index == self.size-1:
            self.removelast()
            return
        
        for itr in range(index):
            pre = head
            head = head.next
        
        pre.next = head.next
        
    def show(self):
        head = self.head
        string = ''
        while head:
            string += str(head.data)+' ,'
            head = head.next
            if head == self.head:
               break
        return ('['+string[:-2]+']')
        
        

    
cll = CLL()

elements = input("Enter the elements : ").split()
for i in elements:
    cll.add_first(int(i))

print("Circular linked list : ",cll.show())

remove = input("Enter index of the element to be removed : ")
cll.removeAt(int(remove))
print("Circular linked list : ",cll.show())

insert = input("Enter the index and element to be inserted : ").split()
cll.insert(int(insert[0]),int(insert[1]))
print("Circular linked list : ",cll.show())

