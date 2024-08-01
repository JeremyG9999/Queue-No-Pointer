class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.isempty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)
    def isempty(self):
        return len(self.items) == 0
    def printQueue(self):
        print(self.items)
def main():
    queues = Queue()
    queues.enqueue(8)
    queues.enqueue(7)
    queues.enqueue(6)
    queues.dequeue()
    print("Queue:")
    queues.printQueue()
main()