from ADT import DoublyLinkedList


def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    if srt_lnk_lst1.is_empty() and srt_lnk_lst2.is_empty():
        raise Exception("DoublyLinkedLists are empty.")
    return merge_sublists(srt_lnk_lst1.first_node(), srt_lnk_lst2.first_node(), DoublyLinkedList.DoublyLinkedList())

def merge_sublists(node1, node2, srt_lst):
    if (node1.data is None) and (node2.data is None):
        return srt_lst
    else:
        if (node1.data is None) or (node2.data is None):
            if (node2.data is None):
                res = node1
            else:
                res = node2
            while res.data is not None:
                srt_lst.add_last(res.data)
                res = res.next
            return srt_lst
        else:
            if node1.data < node2.data:
                srt_lst.add_last(node1.data)
                return merge_sublists(node1.next, node2, srt_lst)
            srt_lst.add_last(node2.data)
            return merge_sublists(node1, node2.next, srt_lst)

