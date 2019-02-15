def intersection_list(lst1, lst2):
    inter_list = []
    lst1.sort()
    lst2.sort()
    cursor1 = 0
    cursor2 = 0
    while cursor1 <= len(lst1)-1 and cursor2 <= len(lst2) - 1:
        if lst1[cursor1] == lst2[cursor2]:
            inter_list.append(lst1[cursor1])
            cursor1 += 1
            cursor2 += 1
        elif lst1[cursor1] > lst2[cursor2]:
            cursor2 += 1
        elif lst1[cursor1] < lst2[cursor2]:
            cursor1 += 1
    return inter_list
