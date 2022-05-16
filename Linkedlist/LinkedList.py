class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LL:

    def __init__(self):
        self.head = None
        self.len = 0

    def add_first(self,data):
        
        self.len +=1
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def add_end(self,data):
        self.len +=1
        itr = self.head
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        while itr:
            if itr.next == None:
                itr.next = node
                return
            itr = itr.next
        return
    
    def add_at(self,index,data):
        
        pos = 0
        node = Node(data)
        itr = self.head
        precedor = None
        while itr:
            if pos == index:
                precedor.next = node
                node.next = itr.next
                return
            precedor = itr
            itr = itr.next
            pos +=1
            
    def show(self):
        
        if self.head == None:
            print("Empty LinkedList.")
            return
        else:
            itr = self.head
            string = ''
            while itr:
                string += str(itr.data)+' ,'
                itr = itr.next
            print('['+string[:-1].strip()+']')

    def length(self):
        print(self.len)

    def index(self,element):
        
        itr = self.head
        position = -1
        while itr:
            position += 1
            if itr.data == element:
                return position
            itr = itr.next
        return "Element not found."

    def at(self,index):
        pos = -1
        itr = self.head
        while itr:
            pos +=1
            if pos == index:
                return itr.data
            itr = itr.next
        return "Out of range."

    def remove(self,element):
        
        itr = self.head
        precedor_node = None
        while itr:
            if itr.data == element:
                
                precedor_node.next = itr.next
                return
            precedor_node = itr
            itr = itr.next
            
    def removeFirst(self):
        temp = self.head
        self.head = temp.next

    def removeLast(self):
        pre = self.head
        curr = self.head
        while curr.next != None:
            pre = curr
            curr = curr.next
        pre.next = None

    def removeMiddle(self,index):
        self.len -=1
        count  = 0
        pre = self.head
        curr = self.head
        while curr.next != None:
            if count == index:
                break
            count +=1
            pre = curr
            curr = curr.next
        print("Removeing : ",self.at(index))
        pre.next = curr.next

ll = LL()
for i in range(11):
    ll.add_first(i)
ll.show()

print("After removing.")
ll.length()
ll.show()
ll.removeMiddle(4)
ll.length()
ll.removeMiddle(5)
ll.length()

ll.show()
