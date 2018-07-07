class Stack():
    def __init__(self,size):
        self.size = size
        self.stack = []
        self.top = -1

    def push(self,x):
        if self.is_full():
            raise Exception("stack is full")
        else:
            self.stack.append(x)
            self.top = self.top+1
            return True

    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty")
        else:
            self.top = self.top-1
            return self.stack.pop()

    def is_full(self):
        return self.top +1 == self.size

    def is_empty(self):
        return self.top == -1

    def show_stack(self):
        print(self.stack)
