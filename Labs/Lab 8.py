class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.is_empty==0:
            raise Exception("Stack is empty")
        return self.data.pop()

    def top(self):
        if self.is_empty==0:
            raise Exception("Stack is empty")
        return self.data[-1]

def balanced_expression(str):
    lst = []
    for i in str:
        lst.append(i)
    opening = "([{"
    closing = ")]}"
    stack = ArrayStack()
    for i in lst:
        if i in opening:
            stack.push(i)
        elif i in closing:
            prev = stack.pop()
            if prev == '(' and i != ")":
                return False
            elif prev == "[" and i != "]":
                return False
            elif prev == '{' and i != '}':
                return False
    if stack.is_empty():
        return True
    else:
        return False

print(balanced_expression("{{([])}}([])("))
print(balanced_expression("{{[(])}}"))



