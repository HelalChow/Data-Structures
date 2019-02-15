from ADT import ArrayStack


class MaxStack:
    def __init__(self):
        self.max_stack_data = ArrayStack.ArrayStack()

    def __len__(self):
        return len(self.max_stack_data)

    def is_empty(self):
        return len(self.max_stack_data) == 0

    def push(self, val):
        if self.is_empty():
            self.max_val = val
            self.max_stack_data.push((val, self.max_val))
        elif val > self.max_val:
            self.max_val = val
            self.max_stack_data.push((val, self.max_val))
        else:
            self.max_stack_data.push((val, self.max_val))

    def top(self):
        last_tuple = self.max_stack_data.top()
        return last_tuple[0]

    def pop(self):
        if (self.max_stack_data.is_empty()):
            raise Exception('MaxStack is Empty')
        last_tuple=self.max_stack_data.pop()
        return last_tuple[0]

    def max(self):
        if (self.max_stack_data.is_empty()):
            raise Exception('MaxStack is Empty')
        last_tuple = self.max_stack_data.top()
        return last_tuple[1]

