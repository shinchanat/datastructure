class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedStack:

    def __init__(self):
        self.head = None
        self.tail= None
        self.length = 0

    def push(self,data):
        self.length +=1
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def peek(self):
        print(self.tail.data)

    def pop(self):
        self.length -=1
        head = self.head
        pre = self.head
        while head.next:
            pre = head
            head = head.next
        pre.next = None
        
    def show(self):
        head = self.head
        while head:

            print(head.data,end=' ')
            head = head.next

    def valueAt(self,index):
        head = self.head
        for i in range(index-1):
            head = head.next
        return head.data

    def insert(self,index,data):
        node = Node(data)
        head = self.head
        pre = self.head
        self.length +=1
        for i in range(index-1):
            pre = head
            head = head.next
        pre.next = node
        node.next = head

linkedstack = LinkedStack()
elements = input("Enter the elements : ").split()
for i in elements:
    linkedstack.push(int(i))
print("LinkedStack : ",end='')
linkedstack.show()
push = int(input("\nEnter the element to be pushed : "))
linkedstack.push(push)
print("LinkedStack : ",end='')
linkedstack.show()
print(f"\nPOPED {linkedstack.valueAt(linkedstack.length)}: ")
linkedstack.pop()
print("LinkedStack : ",end='')
linkedstack.show()
