from ADT import DoublyLinkedList


def copy_linked_list(lnk_lst):
    new = DoublyLinkedList.DoublyLinkedList()
    for i in lnk_lst:
        new.add_last(i)
    return new

def deep_copy_linked_list(lnk_lst):
    new = DoublyLinkedList.DoublyLinkedList()
    for i in lnk_lst:
        if isinstance(i, DoublyLinkedList.DoublyLinkedList):
            curr = deep_copy_linked_list(i)
            new.add_last(curr)
        else:
            new.add_last(i)
    return new
