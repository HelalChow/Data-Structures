from ADT import ArrayQueue, DoublyLinkedList


def reverse_list_change_elements_order(lnk_lst):
    lnk_lst = lnk_lst
    lst = []
    for i in lnk_lst:
        lst.append(i)
    cursor = lnk_lst.header.next
    for i in range(len(lst)-1, -1, -1):
        cursor.data = lst[i]
        cursor = cursor.next


'''test = DoublyLinkedList.DoublyLinkedList()
test.add_last(3)
test.add_last(7)
test.add_last(5)
print(test)

reverse_list_change_elements_order(test)
print(test)'''


def reverse_list_change_nodes_order(lnk_lst):
    front_cursor = lnk_lst.header.next
    back_cursor = lnk_lst.trailer.prev
    for i in range(len(lnk_lst)):
        if front_cursor is not back_cursor:
            hold_back = back_cursor
            hold_front = front_cursor
            front_cursor = hold_front.next
            back_cursor = hold_back.prev
            lnk_lst.add_first(hold_back.data)
            lnk_lst.add_last(hold_front.data)
            lnk_lst.delete_node(hold_back)
            lnk_lst.delete_node(hold_front)


'''test = DoublyLinkedList.DoublyLinkedList()
test.add_last(3)
test.add_last(7)
test.add_last(5)
print(test)

reverse_list_change_nodes_order(test)
print(test)'''

def sum_lnk_lst(lnk_lst):
    new = lnk_lst.delete_first()
    hold = 0
    cursor = lnk_lst.header
    if cursor.next is not lnk_lst.trailer:
        hold = sum_lnk_lst(lnk_lst)
    return new + hold

test = DoublyLinkedList.DoublyLinkedList()
test.add_last(3)
test.add_last(7)
test.add_last(5)
test.add_last(5)

print(test)

sum = sum_lnk_lst(test)
print(sum)

class PlayList:
    def __init__(self):
        self.data = ArrayQueue.ArrayQueue()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def add_to_playlist(self, str_title):
        self.data.enqueue(str_title)

    def print_playlist(self):
        hold = []
        for i in range(len(self)):
            hold.append(self.data.dequeue())
        for i in hold:
            self.data.enqueue(i)
            print("Track" + i)

'''playlist = PlayList()
playlist.add_to_playlist('Track 1: Stairway to Heaven')
playlist.add_to_playlist('Track 3: I Will')
playlist.print_playlist()'''






