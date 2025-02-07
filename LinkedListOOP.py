class Node:
    def __init__(self, givenData: str=None, givenNext: str=None):
        self.data: str = givenData
        self.next: str = givenNext

    def get_data(self) -> str:
        return self.data
    
    def get_next(self) -> str:  
        return self.next
    
    def set_next(self, newNext: str) -> None:
        self.next = newNext


# AppleNode = Node("Apple")
# OrangeNode = Node("Orange")
# PearNode = Node("Pear")

# head = AppleNode
# AppleNode.set_next(OrangeNode)
# OrangeNode.set_next(PearNode)

# current = head
# while current != None:
#     print(current.data)
#     current = current.next

#Part 2:

# abid = Node("Abid")
# dee = Node("Dee")
# peter = Node("Peter")
# tom = Node("Tom")

# head = abid
# abid.set_next(dee)
# dee.set_next(peter)
# peter.set_next(tom)

# current = head  
# while current != None:
#     print(current.data)
#     current = current.next

#part 3:

class LinkedList:
    def __init__(self, head: str=None):
        self.head: str = head

    def insert_data(self, data: str) -> None:
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self) -> int:
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count    
    
    def search(self, data: str) -> bool:
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current
    
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())