import BinarySearchTreeMap

def restore_bst(prefix_lst):
    if len(prefix_lst) == 0:
        bst = BinarySearchTreeMap.BinarySearchTreeMap()
        return bst
    item = BinarySearchTreeMap.BinarySearchTreeMap.Item(prefix_lst[0])
    new_node = BinarySearchTreeMap.BinarySearchTreeMap.Node(item)
    bst = BinarySearchTreeMap.BinarySearchTreeMap()
    bst.root = new_node
    bst.size = 1
    if (len(prefix_lst) > 1):
        restore_bst_helper(bst, bst.root, prefix_lst, 1, len(prefix_lst) - 1)
    return bst

def restore_bst_helper(bst, curr_root, lst, low, high):
    if (low == high):
        item = BinarySearchTreeMap.BinarySearchTreeMap.Item(lst[low])
        new_node = BinarySearchTreeMap.BinarySearchTreeMap.Node(item)
        if (lst[low] < curr_root.item.key):
            curr_root.left = new_node
            bst.size+=1
        else:
            curr_root.right = new_node
            bst.size+=1
    else:
        if (lst[low] > bst.root.item.key):
            item = BinarySearchTreeMap.BinarySearchTreeMap.Item(lst[low])
            new_node = BinarySearchTreeMap.BinarySearchTreeMap.Node(item)
            if (lst[low] < curr_root.item.key):
                curr_root.left = new_node
                new_node.parent = curr_root
                bst.size+=1
                if lst[low+1] < curr_root.item.key:
                    curr_root = new_node
                if (curr_root == bst.root):
                    curr_root = new_node
                restore_bst_helper(bst, curr_root, lst, low + 1, high)
            else:
                curr_root.right = new_node
                new_node.parent = curr_root
                bst.size+=1
                if (curr_root == bst.root):
                    curr_root = new_node
                if lst[low+1] < curr_root.item.key:
                    curr_root = new_node
                restore_bst_helper(bst, curr_root, lst, low + 1, high)
        else:
            item = BinarySearchTreeMap.BinarySearchTreeMap.Item(lst[low])
            new_node = BinarySearchTreeMap.BinarySearchTreeMap.Node(item)
            if (lst[low] < curr_root.item.key):
                curr_root.left = new_node
                new_node.parent = curr_root
                bst.size+=1
                if lst[low+1] < curr_root.item.key:
                    curr_root = new_node
                if (lst[low + 1] > bst.root.item.key):
                    restore_bst_helper(bst, bst.root, lst, low + 1, high)
                else:
                    restore_bst_helper(bst, curr_root, lst, low + 1, high)
            else:
                curr_root.right = new_node
                new_node.parent = curr_root
                bst.size+=1
                if lst[low+1] < curr_root.item.key:
                    curr_root = new_node
                if (lst[low + 1] > bst.root.item.key):
                    restore_bst_helper(bst, bst.root, lst, low + 1, high)
                else:
                    restore_bst_helper(bst, curr_root, lst, low + 1, high)
