from ADT import DoublyLinkedList


class LinkedQueue:
    def __init__(self):
        self.data = DoublyLinkedList.DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return self.data.is_empty()

    def enqueue(self, elem):
        self.data.add_last(elem)

    def dequeue(self):
        if self.is_empty():
            raise Exception("LinkedQueue is empty")
        val = self.data.first_node().data
        self.data.delete_first()
        return val

    def first(self):
        if self.is_empty():
            raise Exception("LinkedQueue is empty")
        return self.data.first_node().data

    def __repr__(self):
        return str(self.data)

