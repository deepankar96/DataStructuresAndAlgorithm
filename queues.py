class Queue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enque(self,data):
        self.queue.append(data)
    
    def deque(self):
        data = self.queue[0]
        del self.queue[0]
        return data

Queue = Queue()
Queue.enque(10)
Queue.enque(20)
Queue.enque(30)
Queue.enque(40)
Queue.enque(50)
print(Queue.deque())
print(Queue.deque())
print(Queue.deque())
print(Queue.deque())
print(Queue.deque())
