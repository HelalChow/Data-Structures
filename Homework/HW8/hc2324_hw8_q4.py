import BinarySearchTreeMap

def find_min_abs_difference(bst):
    lst = []
    for item in bst.inorder():
        lst.append(item.item.key)
    difference = abs(lst[1] - lst[0])
    for i in range(1, len(lst) - 1):
        if abs(lst[i] - lst[i -1]) <= difference:
            difference = abs(lst[i] - lst[i -1])
    return difference