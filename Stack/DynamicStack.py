class DynamicStack:

    def __init__(self,size):
        self.stack = []
        self.size = size

    def push(self,data):
        if len(self.stack)>=self.size:
            print("Doubled StackSize")
            new_stack = list(self.stack)
            new_stack.append(data)
            self.size = self.size*2
            self.stack = new_stack
        else:
            self.stack.append(data)

    def pop(self):
        if not self.stack:
            print("StackUnderFlow")
            return

        self.stack.pop()

    def peek(self):
        if not self.stack:
            print("Empty Stack")
            return
        print(self.stack[-1])

    def size(self):
        print(self.size)

    def show(self):
        return self.stack



size = int(input("Enter the size of the stack : "))
stack = DynamicStack(5)
items = input("Enter the elements : ").split()
for i in items:
    stack.push(int(i))
print("DynamicStack : ",stack.show())

push = int(input("Enter the element to be inserted : "))
stack.push(push)
print("DynamicStack : ",stack.show())

print("Peek element : ",end='')
stack.peek()
