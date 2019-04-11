class Stack:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return self.stack == []
    
    def push(self,data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
Stack = Stack()
Stack.push(20)
Stack.push(30)
Stack.push(40)
Stack.push(1)
print(Stack.size())
print(Stack.peek())
print(Stack.pop())
print(Stack.pop())
print(Stack.pop())

