class Queue: 
    def __init__(self, givenSize: int):
        self.size: int = givenSize
        self.queue: list = [""] * self.size
        self.head: int = 0
        self.tail: int = 0

    def Push(self, givenItem: float) -> list:
        if self.isFull():
            print("Queue is full")
        else:
            self.queue[self.tail] = givenItem
            self.tail += 1
            if self.tail == self.size:
                self.tail = 0
            print(self.queue)

    def Pop(self) -> list:
        if self.isEmpty():
            print("Queue is empty")
        else:
            self.queue[self.head] = ""
            self.head += 1
            if self.head == self.size:
                self.head = 0
            print(self.queue)

    def isFull(self) -> bool:
        if self.head == self.tail + 1:
            return True
        else:
            return False
    
    def isEmpty(self) -> bool:
        if self.head == self.tail:
            return True
        else:
            return False
        
    def Peek(self) -> float:
        return self.queue[self.head]

stack1: Queue = Queue(givenSize=10)
stack1.Pop()
stack1.Push(15)
stack1.Push(37)
stack1.Pop()
print(stack1.Peek())
