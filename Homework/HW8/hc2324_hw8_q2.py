import BinarySearchTreeMap


def create_chain_bst(n):
    tree = BinarySearchTreeMap.BinarySearchTreeMap()
    for i in range(1, n+1):
        tree.insert(i)
    return tree


def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst


def add_items(bst, low, high):
    if low == high:
        bst.insert(low)
    else:
        mid = (low + high) // 2
        bst.insert(mid)
        add_items(bst, low, mid - 1)
        add_items(bst, mid + 1, high)
