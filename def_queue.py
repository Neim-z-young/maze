class Queue():
    def __init__(self,size):
        self.size = size
        self.queue = []
        self.front = -1
        self.rear = -1

    def enqueue(self,x):
        if self.is_full():
            raise Exception("queue is full")
        else:
            self.queue.append(x)
            self.rear = self.rear+1
            return True

    def dequeue(self):
        if self.is_empty():
            raise Exception("queue isempty")
        else:
            self.front = self.front+1
            return self.queue.pop(0)

    def is_full(self):
        return self.rear - self.front+1 == self.size

    def is_empty(self):
        return self.rear == self.front

    def show_queue(self):
        print(self.queue)
