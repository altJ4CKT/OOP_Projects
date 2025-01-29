class Stack:
    def __init__(self, givenSize: int):
        self.size: int = givenSize
        self.stack: list = [""] * self.size
        self.top: int = -1

    def Push(self, givenItem: float) -> list:
        if self.top < self.size -1:
            self.top += 1
            self.stack[self.top] = givenItem
            print(self.stack)
        else:
            print("Stack is full")
    
    def Pop(self) -> list:
        if self.top == -1:
            print("Stack is empty")
        else:
            self.stack[self.top] = ""
            self.top -= 1
            print(self.stack)

    def isFull(self) -> bool:
        if self.top == self.size -1:
            return "Stack is full"
        else:
            return "Stack is not full"  
        
    def isEmpty(self) -> bool:
        if self.top == -1:
            return "Stack is empty"
        else: 
            return "Stack is not empty"
        
    def peek(self) -> float:
        return self.stack[self.top] 

#TESTING
stack1: Stack = Stack(givenSize=10)
stack1.Push(1)
stack1.Push(2)
stack1.Push(3)
stack1.Push(4)
stack1.Push(5)
stack1.Push(6)
print(stack1.isFull())
print(stack1.isEmpty())
print(stack1.peek())







