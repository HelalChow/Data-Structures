from ADT import ArrayQueue, DoublyLinkedList


class LinkedStack():
    def __init__(self):
        self.data = DoublyLinkedList.DoublyLinkedList()
        self.size = 0

    def push(self, elem):
        self.data.add_last(elem)
        self.size += 1

    def pop(self):
        hold = self.data.last_node()
        self.data.delete_last()
        self.size -= 1
        return hold

    def top(self):
        if (self.data.is_empty()):
            raise Exception("List is empty")
        return self.data.last_node()

    def is_empty(self):
        return len(self.data) == 0

    def __len__(self):
        return self.size


class LinkedLeakyStack():
    def __init__(self, max_elems):
        self.data = DoublyLinkedList.DoublyLinkedList()
        self.max = max_elems
        self.size = 0

    def push(self, elem):
        if self.size < self.max:
            self.data.add_last(elem)
            self.size += 1
        else:
            self.data.delete_first()
            self.data.add_first(elem)

    def pop(self):
        if self.data.is_empty():
            raise Exception("List is empty")
        else:
            hold = self.data.last_node()
            self.data.delete_last()
            self.size -= 1
            return hold

    def top(self):
        if self.data.is_empty():
            raise Exception("List is empty")
        else:
            return self.data.last_node()

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size


class ArrayLeakyStack():
    def __init__(self, max_elems):
        self.data = []
        self.max = max_elems
        self.first = None
        self.size = 0

    def push(self, elem):
        if self.size < self.max:
            if self.size == 0:
                self.first = 0
            self.data.append(elem)
            self.size += 1
        else:
            self.data[0] = elem
            self.first = (self.first + 1) % self.max

    def pop(self):
        if self.size == 0:
            raise Exception("List is empty")
        if self.first == 0:
            hold = self.data[self.size-1]
            self.data[self.size - 1] = None
        else:
            hold = self.data[self.first-1]
            self.data[self.first - 1] = None
        self.size -= 1
        return hold

    def top(self):
        if self.size == 0:
            raise Exception("List is empty")
        if self.first == 0:
            hold = self.data[self.size-1]
        else:
            hold = self.data[self.first-1]
        return hold

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __repr__(self):
        return str(self.data)

'''test = ArrayLeakyStack(5)
test.push(2)
test.push(13)
test.push(3)
test.push(8)
test.push(5)

print(test)
print(test.top())

test.push(12)

print(test)
print(test.top())
print(test.pop())'''

class Stack():
    def __init__(self):
        self.data = ArrayQueue.ArrayQueue()


    def push(self, elem):
        if len(self.data) == 0:
            self.data.enqueue(elem)
        else:
            self.data.enqueue(elem)
            for i in range(len(self.data)-1):
                hold = self.data.dequeue()
                self.data.enqueue(hold)

    def pop(self):
        if len(self.data) == 0:
            raise Exception("List is empty")
        hold = self.data.dequeue()
        return hold



test = Stack()
test.push(2)
test.push(13)
test.push(3)
test.push(8)
test.push(5)

print(test.pop())
print(test.pop())
test.push(12)
print(test.pop())