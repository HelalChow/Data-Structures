import ArrayQueue
import DoublyLinkedList

class Queue:
    def __init__(self):
        self.data = ...
        self.order = 1

    def enqueue(self, elem):
        self.data.insert(self.order, elem)
        self.order += 1

    def dequeue(self):
        min = self.data[1][1]
        self.data.delete_min()
        return min

    def first(self):
        return self.data[1][1]

    def __len__(self):
        return len(self.data)-1

    def is_empty(self):
        return len(self) == 0


def print_level(root, level):
    queue = ArrayQueue.ArrayQueue()
    queue.enqueue(root)
    curr_level = 0
    while(curr_level <= level):
        iter = 2**curr_level
        while iter > 0:
            parent = queue.dequeue()
            if parent.left is None and parent.right is None:
                pass
            else:
                queue.enqueue(parent.left)
                queue.enqueue(parent.right)
            iter -= 1
    return [queue.dequeue() for i in range(len(queue))]




class MidStack():
    def __init__(self):
        self.data = DoublyLinkedList.DoublyLinkedList()
        self.mid = DoublyLinkedList.DoublyLinkedList.Node()
        self.data.header.next = self.mid
        self.mid.prev = self.data.header
        self.mid.next = self.data.trailer
        self.data.trailer.prev = self.mid

    def is_empty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)

    def push(self, e):
        node = DoublyLinkedList.DoublyLinkedList.Node(e)
        if len(self) % 2 == 0:
            self.data.add_last(node)
        else:
            self.data.add_last(node)
            curr = self.mid.next
            mid = self.mid
            self.data.delete_node(self.mid)
            self.mid = mid
            self.data.add_after(curr, mid.data)

    def top(self):
        if self.data.trailer.prev is self.mid and self.mid.prev is self.data.header:
            raise Exception("Stack is Empty")
        elif self.data.trailer.prev is self.mid:
            return self.mid.prev
        else:
            return self.data.trailer.prev

    def pop(self):
        if self.data.trailer.prev is self.mid and self.mid.prev is self.data.header:
            raise Exception("Stack is Empty")
        elif self.data.trailer.prev is self.mid:
            last = self.mid.prev
            self.data.delete_node(last)
            return last.data
        else:
            last = self.data.trailer.prev
            self.data.delete_node(last)
            return last.data

    def mid_push(self, e):
        self.data.add_after(self.mid, e)