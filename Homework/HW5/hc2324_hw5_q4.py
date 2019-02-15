from ADT import ArrayStack


class Queue():
    def __init__(self):
        self.rev = ArrayStack.ArrayStack()
        self.order = ArrayStack.ArrayStack()

    def __len__(self):
        return (len(self.rev) + len(self.order))

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, elem):
        self.rev.push(elem)

    def dequeue(self):
        if (self.is_empty()):
            raise Exception("Queue is empty.")
        else:
            while len(self.rev) > 0:
                self.order.push(self.rev.pop())
            val = (self.order.pop())

            while len(self.order) > 0:
                self.rev.push(self.order.pop())

            return val

    def first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty.")
        else:
            while len(self.rev) > 0:
                self.order.push(self.rev.pop())
            val = (self.order.top())

            while len(self.order) > 0:
                self.rev.push(self.order.pop())
            return val
