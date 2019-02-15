import ChainingHashTableMap

def intersection_list(lst1, lst2):
    cht_lst1 = ChainingHashTableMap.ChainingHashTableMap()
    intersection_lst = []
    for elem in lst1:
        cht_lst1[elem] = None
    for other_elem in lst2:
        old_len = len(cht_lst1)
        cht_lst1[other_elem] = None
        new_len = len(cht_lst1)
        if old_len == new_len:
            intersection_lst.append(other_elem)
    return intersection_lst

