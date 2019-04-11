class Node(object):

    def __init__(self,data):
        self.data = data
        self.nextNode = None
    
class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

#O(1)
    def insertStart(self,data):
        self.size += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
#O(1)
    def sizeLinkedList(self):
        return self.size
#O(N)    
    def insertEnd(self,data):
        self.size += 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        
        actualNode.nextNode = newNode
#O(N)
    def traverse(self):
        actualNode = self.head
        
        while actualNode is not None:
            print(actualNode.data)
            actualNode = actualNode.nextNode
#O(N)
    def remove(self,data):
        if self.head is None:
            return 
        
        self.size -= 1
        currentNode = self.head
        previousNode = None

        while currentNode.data !=data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode


LinkedList = LinkedList()
LinkedList.insertStart(20)
LinkedList.insertStart(30)
LinkedList.insertEnd(40)
LinkedList.traverse()
print(LinkedList.sizeLinkedList())
print ()
LinkedList.remove(20)
LinkedList.traverse()
LinkedList.remove(40)
print ()
LinkedList.traverse()