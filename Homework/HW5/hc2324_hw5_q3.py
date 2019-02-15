from ADT import ArrayDeque, ArrayStack


class MidStack:
    def __init__(self):
        self.top_half = ArrayDeque.ArrayDeque()
        self.bottom_half = ArrayStack.ArrayStack()

    def __len__(self):
        return len(self.top_half) + len(self.bottom_half)

    def is_empty(self):
        return (len(self) == 0)

    def push(self, elem):
        self.top_half.enqueue_last(elem)

    def top(self):
        if (self.is_empty()):
            raise Exception("Midstack is empty.")
        else:
            if (self.top_half.is_empty()):
                return self.bottom_half.top()
            else:
                return self.top_half.last()

    def pop(self):
        if (self.is_empty()):
            raise Exception("Midtack is empty.")
        else:
            if (self.top_half.is_empty()):
                return self.bottom_half.pop()
            else:
                return self.top_half.dequeue_last()

    def mid_push(self, elem):
        if len(self.bottom_half) == len(self.top_half):
            self.top_half.add_first(elem)

        else:
            while len(self.top_half) > len(self.bottom_half):
                self.bottom_half.push(self.top_half.dequeue_first())
            self.bottom_half.push(elem)
