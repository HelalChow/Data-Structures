class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        self.tail = next
        self.prev = None


head1 = None
head1 = Node()
head1.data = 1
head1.next = Node()
head1.next.data = 2
head1.next.next = Node()
head1.next.next.data = 3

print()

node = head1

while node is not None:
    print(node.data)
    node = node.next

curr = Node()
curr.data = 4
curr.next = head1
head1 = curr

def add_first(lnk_lst_head, val):
    curr = Node()
    curr.data = val
    curr.next = lnk_lst_head
    return curr


head1 = add_first(head1, 5)
head1 = add_first(head1, 6)
print(head1)